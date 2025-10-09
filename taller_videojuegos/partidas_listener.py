# partidas_listener.py
from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from generated.CSVListener import CSVListener
import json, math, sys
from collections import defaultdict

# Utilidad segura para números enteros
def _to_int(val, field_name, line, errors):
    s = (val or "").strip().replace('"', '')
    if s == "":
        errors.append(f"[Semántico][L{line}] Campo '{field_name}' vacío.")
        return None
    try:
        return int(s)
    except ValueError:
        errors.append(f"[Semántico][L{line}] Campo '{field_name}' no es entero válido: '{s}'.")
        return None

class PartidasListener(CSVListener):
    """
    Listener ANTLR4:
    - exitHeader: capturo cabecera.
    - exitRow: valido, transformo, calculo KDA, agrupo por jugador y acumulo estadísticas.
    - exitText/exitString/exitEmpty: recojo celdas.
    """

    CAMPOS_REQUERIDOS = ["Jugador", "Asesinatos", "Muertes", "Asistencias", "Resultado"]
    RESULTADOS_VALIDOS = {"Victoria", "Derrota"}

    def __init__(self, redondeo=2):
        self.header = []
        self.currentRowFieldValues = []
        self.errors = []

        # Estructuras de salida
        self.grouped = defaultdict(lambda: {"partidas": []})

        # Acumuladores (>= 5 estadísticas)
        self.total_partidas = 0
        self.partidas_por_jugador = defaultdict(int)
        self.victorias_por_jugador = defaultdict(int)
        self.derrotas_por_jugador = defaultdict(int)
        self.kda_sum_por_jugador = defaultdict(float)
        self.kda_count_por_jugador = defaultdict(int)
        self.kills_sum = 0
        self.deaths_sum = 0
        self.assists_sum = 0
        self.redondeo = redondeo

        # Aux para duplicados (opcional)
        self._rows_seen = set()

    # ====== Captura de campos por fila ======
    def enterRow(self, ctx:CSVParser.RowContext):
        self.currentRowFieldValues = []

    def exitText(self, ctx:CSVParser.TextContext):
        self.currentRowFieldValues.append(ctx.getText())

    def exitString(self, ctx:CSVParser.StringContext):
        text = ctx.getText()[1:-1].replace('""', '"')
        self.currentRowFieldValues.append(text)

    def exitEmpty(self, ctx:CSVParser.EmptyContext):
        self.currentRowFieldValues.append("")

    # ====== Cabecera ======
    def exitHeader(self, ctx:CSVParser.HeaderContext):
        self.header = list(self.currentRowFieldValues)
        # Validación mínima de cabecera
        faltantes = [c for c in self.CAMPOS_REQUERIDOS if c not in self.header]
        if faltantes:
            self.errors.append(f"[Sintáctico] Cabecera no contiene columnas requeridas: {faltantes}")
        self.currentRowFieldValues = []

    # ====== Fila de datos ======
    def exitRow(self, ctx:CSVParser.RowContext):
        # Ignorar la fila que pertenece a la cabecera
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            return

        # Validación de conteo de columnas
        if len(self.currentRowFieldValues) != len(self.header):
            self.errors.append(
                f"[Semántico][L{ctx.start.line}] "
                f"Nº columnas={len(self.currentRowFieldValues)} difiere de cabecera={len(self.header)}. Fila omitida."
            )
            return

        row = dict(zip(self.header, self.currentRowFieldValues))

        # Detección de duplicados exactos (opcional)
        row_tuple = tuple(row.get(k, "") for k in self.header)
        if row_tuple in self._rows_seen:
            # Podría contarse, advertir, etc. Aquí solo aviso y continúo (o return para omitir).
            self.errors.append(f"[Semántico][L{ctx.start.line}] Fila duplicada detectada.")
            # return
        else:
            self._rows_seen.add(row_tuple)

        # ===== Validaciones y transformaciones de dominio =====
        jugador = (row.get("Jugador") or "").strip()
        if not jugador:
            self.errors.append(f"[Semántico][L{ctx.start.line}] 'Jugador' vacío. Fila omitida.")
            return

        ases = _to_int(row.get("Asesinatos"), "Asesinatos", ctx.start.line, self.errors)
        muer = _to_int(row.get("Muertes"), "Muertes", ctx.start.line, self.errors)
        asis = _to_int(row.get("Asistencias"), "Asistencias", ctx.start.line, self.errors)
        if None in (ases, muer, asis):
            return  # fila inválida

        resultado = (row.get("Resultado") or "").strip().title()
        if resultado not in self.RESULTADOS_VALIDOS:
            self.errors.append(
                f"[Semántico][L{ctx.start.line}] 'Resultado' inválido: '{resultado}'. Use Victoria/Derrota."
            )
            return

        # Cálculo de KDA: (asesinatos + asistencias) / max(1, muertes)
        denom = max(1, muer)
        kda_val = (ases + asis) / denom
        # redondeo controlado
        kda_val = round(kda_val + 1e-12, self.redondeo)

        # Agregar al agrupado por jugador (RI específica + "generación")
        self.grouped[jugador]["partidas"].append({
            "asesinatos": ases,
            "muertes": muer,
            "asistencias": asis,
            "resultado": resultado,
            "kda": kda_val
        })

        # ===== Estadísticas acumuladas =====
        self.total_partidas += 1
        self.partidas_por_jugador[jugador] += 1
        if resultado == "Victoria":
            self.victorias_por_jugador[jugador] += 1
        else:
            self.derrotas_por_jugador[jugador] += 1

        self.kda_sum_por_jugador[jugador] += kda_val
        self.kda_count_por_jugador[jugador] += 1

        self.kills_sum += ases
        self.deaths_sum += muer
        self.assists_sum += asis

    # ====== API de salida ======
    def grouped_output(self):
        # Devolver un dict normal
        return {k: v for k, v in self.grouped.items()}

    def stats(self):
        # kda promedio por jugador y winrate
        kda_prom = {}
        winrate = {}
        for j in self.kda_sum_por_jugador:
            c = self.kda_count_por_jugador[j]
            kda_prom[j] = round(self.kda_sum_por_jugador[j] / c, self.redondeo) if c else 0.0

        for j in self.partidas_por_jugador:
            p = self.partidas_por_jugador[j]
            w = self.victorias_por_jugador[j]
            winrate[j] = round((w / p) * 100.0, 2) if p else 0.0

        # mejor KDA global (promedio)
        mejor_j = None
        mejor_k = -math.inf
        for j, k in kda_prom.items():
            if k > mejor_k:
                mejor_k, mejor_j = k, j

        # promedios globales
        prom_muertes = round(self.deaths_sum / self.total_partidas, 2) if self.total_partidas else 0.0
        prom_asist   = round(self.assists_sum / self.total_partidas, 2) if self.total_partidas else 0.0

        return {
            "total_partidas": self.total_partidas,
            "partidas_por_jugador": dict(self.partidas_por_jugador),
            "victorias_por_jugador": dict(self.victorias_por_jugador),
            "derrotas_por_jugador": dict(self.derrotas_por_jugador),
            "kda_promedio_por_jugador": kda_prom,
            "winrate_por_jugador_%": winrate,
            "mejor_kda_promedio_global": {"jugador": mejor_j, "kda": mejor_k if mejor_k>-math.inf else 0.0},
            "promedio_muertes_global": prom_muertes,
            "promedio_asistencias_global": prom_asist,
            "errores": list(self.errors),
        }

    def write_json(self, filename="salida.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.grouped_output(), f, indent=2, ensure_ascii=False)