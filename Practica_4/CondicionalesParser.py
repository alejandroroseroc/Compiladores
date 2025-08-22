# Generated from Condicionales.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,4,3,35,8,3,11,3,12,3,36,1,3,1,3,1,4,
        1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,54,8,6,1,6,1,
        6,1,6,1,6,1,6,1,6,5,6,62,8,6,10,6,12,6,65,9,6,1,6,0,1,12,7,0,2,4,
        6,8,10,12,0,1,1,0,8,13,66,0,15,1,0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,
        6,28,1,0,0,0,8,40,1,0,0,0,10,44,1,0,0,0,12,53,1,0,0,0,14,16,3,2,
        1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,
        1,0,0,0,19,22,3,4,2,0,20,22,3,6,3,0,21,19,1,0,0,0,21,20,1,0,0,0,
        22,3,1,0,0,0,23,24,5,16,0,0,24,25,5,1,0,0,25,26,3,12,6,0,26,27,5,
        2,0,0,27,5,1,0,0,0,28,29,5,3,0,0,29,30,5,4,0,0,30,31,3,8,4,0,31,
        32,5,5,0,0,32,34,5,6,0,0,33,35,3,2,1,0,34,33,1,0,0,0,35,36,1,0,0,
        0,36,34,1,0,0,0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,5,7,0,0,39,7,1,
        0,0,0,40,41,3,12,6,0,41,42,3,10,5,0,42,43,3,12,6,0,43,9,1,0,0,0,
        44,45,7,0,0,0,45,11,1,0,0,0,46,47,6,6,-1,0,47,54,5,16,0,0,48,54,
        5,17,0,0,49,50,5,4,0,0,50,51,3,12,6,0,51,52,5,5,0,0,52,54,1,0,0,
        0,53,46,1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,54,63,1,0,0,0,55,56,
        10,5,0,0,56,57,5,14,0,0,57,62,3,12,6,6,58,59,10,4,0,0,59,60,5,15,
        0,0,60,62,3,12,6,5,61,55,1,0,0,0,61,58,1,0,0,0,62,65,1,0,0,0,63,
        61,1,0,0,0,63,64,1,0,0,0,64,13,1,0,0,0,65,63,1,0,0,0,6,17,21,36,
        53,61,63
    ]

class CondicionalesParser ( Parser ):

    grammarFileName = "Condicionales.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'if'", "'('", "')'", "'{'", 
                     "'}'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'+'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_asignacion = 2
    RULE_condicional = 3
    RULE_condicion = 4
    RULE_operadorComp = 5
    RULE_expresion = 6

    ruleNames =  [ "programa", "sentencia", "asignacion", "condicional", 
                   "condicion", "operadorComp", "expresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    ID=16
    NUMBER=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CondicionalesParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CondicionalesParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CondicionalesParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = CondicionalesParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.sentencia()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==16):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(CondicionalesParser.AsignacionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(CondicionalesParser.CondicionalContext,0)


        def getRuleIndex(self):
            return CondicionalesParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = CondicionalesParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.asignacion()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.condicional()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CondicionalesParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(CondicionalesParser.ExpresionContext,0)


        def getRuleIndex(self):
            return CondicionalesParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = CondicionalesParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(CondicionalesParser.ID)
            self.state = 24
            self.match(CondicionalesParser.T__0)
            self.state = 25
            self.expresion(0)
            self.state = 26
            self.match(CondicionalesParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicion(self):
            return self.getTypedRuleContext(CondicionalesParser.CondicionContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CondicionalesParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CondicionalesParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CondicionalesParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = CondicionalesParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(CondicionalesParser.T__2)
            self.state = 29
            self.match(CondicionalesParser.T__3)
            self.state = 30
            self.condicion()
            self.state = 31
            self.match(CondicionalesParser.T__4)
            self.state = 32
            self.match(CondicionalesParser.T__5)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.sentencia()
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==16):
                    break

            self.state = 38
            self.match(CondicionalesParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CondicionalesParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CondicionalesParser.ExpresionContext,i)


        def operadorComp(self):
            return self.getTypedRuleContext(CondicionalesParser.OperadorCompContext,0)


        def getRuleIndex(self):
            return CondicionalesParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = CondicionalesParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.expresion(0)
            self.state = 41
            self.operadorComp()
            self.state = 42
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorCompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CondicionalesParser.RULE_operadorComp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorComp" ):
                listener.enterOperadorComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorComp" ):
                listener.exitOperadorComp(self)




    def operadorComp(self):

        localctx = CondicionalesParser.OperadorCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operadorComp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CondicionalesParser.ID, 0)

        def NUMBER(self):
            return self.getToken(CondicionalesParser.NUMBER, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CondicionalesParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CondicionalesParser.ExpresionContext,i)


        def getRuleIndex(self):
            return CondicionalesParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CondicionalesParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 47
                self.match(CondicionalesParser.ID)
                pass
            elif token in [17]:
                self.state = 48
                self.match(CondicionalesParser.NUMBER)
                pass
            elif token in [4]:
                self.state = 49
                self.match(CondicionalesParser.T__3)
                self.state = 50
                self.expresion(0)
                self.state = 51
                self.match(CondicionalesParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CondicionalesParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 55
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 56
                        self.match(CondicionalesParser.T__13)
                        self.state = 57
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = CondicionalesParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 58
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 59
                        self.match(CondicionalesParser.T__14)
                        self.state = 60
                        self.expresion(5)
                        pass

             
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




