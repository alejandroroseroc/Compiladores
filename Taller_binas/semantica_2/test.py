# run_tests.py
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from contextlib import redirect_stdout
import io

from generated.IfElseLangLexer import IfElseLangLexer
from generated.IfElseLangParser import IfElseLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor

class FailFastErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Lanzamos excepción para marcar fallo de sintaxis
        raise Exception(f"Error de sintaxis en {line}:{column} - {msg}")

def parse_and_visit(code: str):
    """
    Devuelve (ok_semantic, semantic_output)
    ok_semantic = True si NO se imprimieron errores semánticos.
    """
    # 1) Lex y parse con errores de sintaxis como excepción
    input_stream = InputStream(code)
    lexer = IfElseLangLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(FailFastErrorListener())

    tokens = CommonTokenStream(lexer)
    parser = IfElseLangParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(FailFastErrorListener())

    tree = parser.program()

    # 2) Visitar capturando stdout para detectar prints de error
    buf = io.StringIO()
    visitor = SemanticVisitor()
    with redirect_stdout(buf):
        visitor.visit(tree)
    out = buf.getvalue().strip()

    # Criterio simple: si el visitor imprimió algo con "Error Semántico", consideramos fallo
    ok = ("Error Semántico" not in out)
    return ok, out

# ---------------------------
# TESTS
# ---------------------------

TESTS = [
    # --- Ejercicio 1: Válido (tu input largo) ---
    {
        "name": "OK: Programa válido con funciones, params, return, if/else",
        "expect_ok": True,
        "code": r"""
// Declaración de una función que suma dos enteros.
int suma(int a, int b) {
    int resultado_local = 0;
    resultado_local = a + b;
    return resultado_local;
}

// Declaración de una función que concatena un saludo.
string saludar(string nombre) {
    string resultado_local = "";
    resultado_local = "Hola " + nombre;
    return resultado_local;
}

// Variables globales.
int total = 0;
string mensaje = "";
int umbral = 15;

// Llamada a función y asignación.
total = suma(10, 5);

// Uso de llamada a función en una condición.
if (total > umbral) {
    mensaje = saludar("Mundo");
} else {
    mensaje = saludar("Clase");
}

// Redeclaración válida en un ámbito diferente.
int a = 100;
        """
    },

    # --- Casos adicionales útiles para este ejercicio ---

    # Llamada con número incorrecto de argumentos
    {
        "name": "ERR: número de argumentos incorrecto",
        "expect_ok": False,
        "code": r"""
int suma(int a, int b) { return a + b; }
int x = 0;
x = suma(1); // falta un argumento
        """
    },

    # Tipos de argumentos incorrectos
    {
        "name": "ERR: tipos de argumentos incorrectos",
        "expect_ok": False,
        "code": r"""
int suma(int a, int b) { return a + b; }
int x = 0;
x = suma("uno", 2); // "uno" no es int
        """
    },

    # Return de tipo incorrecto
    {
        "name": "ERR: tipo de retorno incorrecto",
        "expect_ok": False,
        "code": r"""
int foo() {
    return "hola"; // debería ser int
}
        """
    },

    # Uso de función como variable
    {
        "name": "ERR: usar nombre de función como variable",
        "expect_ok": False,
        "code": r"""
int foo() { return 1; }
int x = foo; // no se puede usar función como variable
        """
    },

    # Asignar a una función
    {
        "name": "ERR: asignar a una función",
        "expect_ok": False,
        "code": r"""
int foo() { return 1; }
foo = 3; // no se puede
        """
    },

    # Llamar identificador que NO es función
    {
        "name": "ERR: llamar a identificador que no es función",
        "expect_ok": False,
        "code": r"""
int x = 10;
x(1,2); // x no es función
        """
    },
]

def main():
    total = len(TESTS)
    passed = 0
    print("="*80)
    print("EJECUTANDO TESTS\n")
    for t in TESTS:
        name = t["name"]
        expect_ok = t["expect_ok"]
        code = t["code"]

        try:
            ok, out = parse_and_visit(code)
            status = "PASS" if ok == expect_ok else "FAIL"
        except Exception as e:
            # Si hay error de sintaxis, lo consideramos FAIL salvo que esperáramos error
            ok = False
            out = f"(Excepción) {e}"
            status = "PASS" if ok == expect_ok else "FAIL"

        if status == "PASS":
            passed += 1

        print(f"[{status}] {name}")
        if out:
            print(out)
        print("-"*80)

    print(f"\nResumen: {passed}/{total} tests correctos.")
    print("="*80)

if __name__ == "__main__":
    main()
