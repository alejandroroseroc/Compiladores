# Generated from Condicionales.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CondicionalesParser import CondicionalesParser
else:
    from CondicionalesParser import CondicionalesParser

# This class defines a complete listener for a parse tree produced by CondicionalesParser.
class CondicionalesListener(ParseTreeListener):

    # Enter a parse tree produced by CondicionalesParser#programa.
    def enterPrograma(self, ctx:CondicionalesParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CondicionalesParser#programa.
    def exitPrograma(self, ctx:CondicionalesParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CondicionalesParser#sentencia.
    def enterSentencia(self, ctx:CondicionalesParser.SentenciaContext):
        pass

    # Exit a parse tree produced by CondicionalesParser#sentencia.
    def exitSentencia(self, ctx:CondicionalesParser.SentenciaContext):
        pass


    # Enter a parse tree produced by CondicionalesParser#asignacion.
    def enterAsignacion(self, ctx:CondicionalesParser.AsignacionContext):
        pass

    # Exit a parse tree produced by CondicionalesParser#asignacion.
    def exitAsignacion(self, ctx:CondicionalesParser.AsignacionContext):
        pass


    # Enter a parse tree produced by CondicionalesParser#condicional.
    def enterCondicional(self, ctx:CondicionalesParser.CondicionalContext):
        pass

    # Exit a parse tree produced by CondicionalesParser#condicional.
    def exitCondicional(self, ctx:CondicionalesParser.CondicionalContext):
        pass


    # Enter a parse tree produced by CondicionalesParser#condicion.
    def enterCondicion(self, ctx:CondicionalesParser.CondicionContext):
        pass

    # Exit a parse tree produced by CondicionalesParser#condicion.
    def exitCondicion(self, ctx:CondicionalesParser.CondicionContext):
        pass


    # Enter a parse tree produced by CondicionalesParser#operadorComp.
    def enterOperadorComp(self, ctx:CondicionalesParser.OperadorCompContext):
        pass

    # Exit a parse tree produced by CondicionalesParser#operadorComp.
    def exitOperadorComp(self, ctx:CondicionalesParser.OperadorCompContext):
        pass


    # Enter a parse tree produced by CondicionalesParser#expresion.
    def enterExpresion(self, ctx:CondicionalesParser.ExpresionContext):
        pass

    # Exit a parse tree produced by CondicionalesParser#expresion.
    def exitExpresion(self, ctx:CondicionalesParser.ExpresionContext):
        pass



del CondicionalesParser