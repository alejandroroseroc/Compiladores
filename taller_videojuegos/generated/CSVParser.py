# Generated from CSV.g4 by ANTLR 4.13.2
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
        4,1,6,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,3,0,19,8,0,1,1,1,1,1,2,1,2,1,2,5,2,26,8,
        2,10,2,12,2,29,9,2,1,2,3,2,32,8,2,1,2,1,2,1,3,1,3,1,3,5,3,39,8,3,
        10,3,12,3,42,9,3,1,4,1,4,1,4,3,4,47,8,4,1,4,0,0,5,0,2,4,6,8,0,0,
        50,0,10,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,35,1,0,0,0,8,46,1,0,
        0,0,10,14,3,2,1,0,11,13,3,4,2,0,12,11,1,0,0,0,13,16,1,0,0,0,14,12,
        1,0,0,0,14,15,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,17,19,3,6,3,0,
        18,17,1,0,0,0,18,19,1,0,0,0,19,1,1,0,0,0,20,21,3,4,2,0,21,3,1,0,
        0,0,22,27,3,8,4,0,23,24,5,1,0,0,24,26,3,8,4,0,25,23,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,
        30,32,5,2,0,0,31,30,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,5,
        3,0,0,34,5,1,0,0,0,35,40,3,8,4,0,36,37,5,1,0,0,37,39,3,8,4,0,38,
        36,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,7,1,0,0,
        0,42,40,1,0,0,0,43,47,5,4,0,0,44,47,5,5,0,0,45,47,1,0,0,0,46,43,
        1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,9,1,0,0,0,6,14,18,27,31,40,
        46
    ]

class CSVParser ( Parser ):

    grammarFileName = "CSV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'\\r'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "STRING", "WS" ]

    RULE_csvFile = 0
    RULE_header = 1
    RULE_row = 2
    RULE_lastRow = 3
    RULE_field = 4

    ruleNames =  [ "csvFile", "header", "row", "lastRow", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TEXT=4
    STRING=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CsvFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(CSVParser.HeaderContext,0)


        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.RowContext)
            else:
                return self.getTypedRuleContext(CSVParser.RowContext,i)


        def lastRow(self):
            return self.getTypedRuleContext(CSVParser.LastRowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_csvFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsvFile" ):
                listener.enterCsvFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsvFile" ):
                listener.exitCsvFile(self)




    def csvFile(self):

        localctx = CSVParser.CsvFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_csvFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.header()
            self.state = 14
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 11
                    self.row() 
                self.state = 16
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 17
                self.lastRow()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(CSVParser.RowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)




    def header(self):

        localctx = CSVParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.row()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.field()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 23
                self.match(CSVParser.T__0)
                self.state = 24
                self.field()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 30
                self.match(CSVParser.T__1)


            self.state = 33
            self.match(CSVParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LastRowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_lastRow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastRow" ):
                listener.enterLastRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastRow" ):
                listener.exitLastRow(self)




    def lastRow(self):

        localctx = CSVParser.LastRowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lastRow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.field()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 36
                self.match(CSVParser.T__0)
                self.state = 37
                self.field()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVParser.RULE_field

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CSVParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class TextContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(CSVParser.TEXT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)


    class EmptyContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)



    def field(self):

        localctx = CSVParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = CSVParser.TextContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(CSVParser.TEXT)
                pass
            elif token in [5]:
                localctx = CSVParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(CSVParser.STRING)
                pass
            elif token in [-1, 1, 2, 3]:
                localctx = CSVParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)

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





