# Generated from Asignaciones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AsignacionesParser import AsignacionesParser
else:
    from AsignacionesParser import AsignacionesParser

# This class defines a complete listener for a parse tree produced by AsignacionesParser.
class AsignacionesListener(ParseTreeListener):

    # Enter a parse tree produced by AsignacionesParser#programa.
    def enterPrograma(self, ctx:AsignacionesParser.ProgramaContext):
        pass

    # Exit a parse tree produced by AsignacionesParser#programa.
    def exitPrograma(self, ctx:AsignacionesParser.ProgramaContext):
        pass


    # Enter a parse tree produced by AsignacionesParser#asignacion.
    def enterAsignacion(self, ctx:AsignacionesParser.AsignacionContext):
        pass

    # Exit a parse tree produced by AsignacionesParser#asignacion.
    def exitAsignacion(self, ctx:AsignacionesParser.AsignacionContext):
        pass


    # Enter a parse tree produced by AsignacionesParser#expresion.
    def enterExpresion(self, ctx:AsignacionesParser.ExpresionContext):
        pass

    # Exit a parse tree produced by AsignacionesParser#expresion.
    def exitExpresion(self, ctx:AsignacionesParser.ExpresionContext):
        pass



del AsignacionesParser