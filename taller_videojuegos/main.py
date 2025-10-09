# main.py
import sys, json
from antlr4 import *
from generated.CSVLexer import CSVLexer
from generated.CSVParser import CSVParser
from partidas_listener import PartidasListener

def run(csv_path):
    # FASE 1: Léxico
    input_stream = FileStream(csv_path, encoding="utf-8")
    lexer = CSVLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    # FASE 2: Sintáctico
    parser = CSVParser(tokens)
    tree = parser.csvFile()

    # FASE 3 + 4: Listener (semántico) + RI + generación JSON
    listener = PartidasListener(redondeo=2)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Escribir JSON agrupado
    listener.write_json("salida.json")

    # Imprimir stats
    s = listener.stats()
    print("\n=== ESTADÍSTICAS ===")
    print(json.dumps(s, indent=2, ensure_ascii=False))
    print("\n✔ JSON generado en 'salida.json'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py datos.csv")
        sys.exit(1)
    run(sys.argv[1])