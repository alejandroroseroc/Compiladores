# Generated from WhileLang.g4 by ANTLR 4.13.2
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
        4,1,28,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,3,1,36,8,1,1,1,1,1,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,1,4,1,4,1,4,3,4,56,8,
        4,1,5,1,5,5,5,60,8,5,10,5,12,5,63,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,79,8,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,101,8,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,109,8,11,10,
        11,12,11,112,9,11,1,11,0,1,22,12,0,2,4,6,8,10,12,14,16,18,20,22,
        0,4,1,0,1,2,2,0,14,15,18,19,1,0,14,19,1,0,20,23,117,0,25,1,0,0,0,
        2,31,1,0,0,0,4,39,1,0,0,0,6,48,1,0,0,0,8,55,1,0,0,0,10,57,1,0,0,
        0,12,66,1,0,0,0,14,71,1,0,0,0,16,80,1,0,0,0,18,86,1,0,0,0,20,89,
        1,0,0,0,22,100,1,0,0,0,24,26,3,6,3,0,25,24,1,0,0,0,26,27,1,0,0,0,
        27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,
        0,0,31,32,3,4,2,0,32,35,5,24,0,0,33,34,5,13,0,0,34,36,3,22,11,0,
        35,33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,5,12,0,0,38,3,1,
        0,0,0,39,40,7,0,0,0,40,5,1,0,0,0,41,49,3,12,6,0,42,49,3,14,7,0,43,
        49,3,16,8,0,44,49,3,2,1,0,45,49,3,18,9,0,46,49,3,20,10,0,47,49,3,
        10,5,0,48,41,1,0,0,0,48,42,1,0,0,0,48,43,1,0,0,0,48,44,1,0,0,0,48,
        45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,7,1,0,0,0,50,56,3,22,11,
        0,51,52,3,22,11,0,52,53,7,1,0,0,53,54,3,22,11,0,54,56,1,0,0,0,55,
        50,1,0,0,0,55,51,1,0,0,0,56,9,1,0,0,0,57,61,5,10,0,0,58,60,3,6,3,
        0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,
        1,0,0,0,63,61,1,0,0,0,64,65,5,11,0,0,65,11,1,0,0,0,66,67,5,24,0,
        0,67,68,5,13,0,0,68,69,3,22,11,0,69,70,5,12,0,0,70,13,1,0,0,0,71,
        72,5,3,0,0,72,73,5,8,0,0,73,74,3,22,11,0,74,75,5,9,0,0,75,78,3,10,
        5,0,76,77,5,4,0,0,77,79,3,10,5,0,78,76,1,0,0,0,78,79,1,0,0,0,79,
        15,1,0,0,0,80,81,5,5,0,0,81,82,5,8,0,0,82,83,3,22,11,0,83,84,5,9,
        0,0,84,85,3,10,5,0,85,17,1,0,0,0,86,87,5,6,0,0,87,88,5,12,0,0,88,
        19,1,0,0,0,89,90,5,7,0,0,90,91,5,12,0,0,91,21,1,0,0,0,92,93,6,11,
        -1,0,93,101,5,24,0,0,94,101,5,25,0,0,95,101,5,26,0,0,96,97,5,8,0,
        0,97,98,3,22,11,0,98,99,5,9,0,0,99,101,1,0,0,0,100,92,1,0,0,0,100,
        94,1,0,0,0,100,95,1,0,0,0,100,96,1,0,0,0,101,110,1,0,0,0,102,103,
        10,3,0,0,103,104,7,2,0,0,104,109,3,22,11,4,105,106,10,2,0,0,106,
        107,7,3,0,0,107,109,3,22,11,3,108,102,1,0,0,0,108,105,1,0,0,0,109,
        112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,23,1,0,0,0,112,110,
        1,0,0,0,9,27,35,48,55,61,78,100,108,110
    ]

class WhileLangParser ( Parser ):

    grammarFileName = "WhileLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'string'", "'if'", "'else'", 
                     "'while'", "'break'", "'continue'", "'('", "')'", "'{'", 
                     "'}'", "';'", "'='", "'<'", "'>'", "'>='", "'<='", 
                     "'=='", "'!='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELSE", 
                      "WHILE", "BREAK", "CONTINUE", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "SEMI", "ASSIGN", "LT", "GT", 
                      "GE", "LE", "EQ", "NE", "PLUS", "MINUS", "MUL", "DIV", 
                      "ID", "NUMBER", "STRING", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_type = 2
    RULE_statement = 3
    RULE_condition = 4
    RULE_block = 5
    RULE_assignment = 6
    RULE_ifStatement = 7
    RULE_whileStatement = 8
    RULE_breakStatement = 9
    RULE_continueStatement = 10
    RULE_expr = 11

    ruleNames =  [ "program", "declaration", "type", "statement", "condition", 
                   "block", "assignment", "ifStatement", "whileStatement", 
                   "breakStatement", "continueStatement", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    ELSE=4
    WHILE=5
    BREAK=6
    CONTINUE=7
    LPAREN=8
    RPAREN=9
    LBRACE=10
    RBRACE=11
    SEMI=12
    ASSIGN=13
    LT=14
    GT=15
    GE=16
    LE=17
    EQ=18
    NE=19
    PLUS=20
    MINUS=21
    MUL=22
    DIV=23
    ID=24
    NUMBER=25
    STRING=26
    COMMENT=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WhileLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = WhileLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16778478) != 0)):
                    break

            self.state = 29
            self.match(WhileLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(WhileLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(WhileLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = WhileLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.type_()
            self.state = 32
            self.match(WhileLangParser.ID)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 33
                self.match(WhileLangParser.ASSIGN)
                self.state = 34
                self.expr(0)


            self.state = 37
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = WhileLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(WhileLangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(WhileLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(WhileLangParser.WhileStatementContext,0)


        def declaration(self):
            return self.getTypedRuleContext(WhileLangParser.DeclarationContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(WhileLangParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(WhileLangParser.ContinueStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(WhileLangParser.BlockContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = WhileLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.ifStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.whileStatement()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.declaration()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.breakStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.continueStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 47
                self.block()
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


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)


        def GT(self):
            return self.getToken(WhileLangParser.GT, 0)

        def LT(self):
            return self.getToken(WhileLangParser.LT, 0)

        def EQ(self):
            return self.getToken(WhileLangParser.EQ, 0)

        def NE(self):
            return self.getToken(WhileLangParser.NE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = WhileLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.expr(0)
                self.state = 52
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 835584) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 53
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(WhileLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(WhileLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = WhileLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(WhileLangParser.LBRACE)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16778478) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(WhileLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(WhileLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = WhileLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(WhileLangParser.ID)
            self.state = 67
            self.match(WhileLangParser.ASSIGN)
            self.state = 68
            self.expr(0)
            self.state = 69
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(WhileLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(WhileLangParser.ELSE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = WhileLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(WhileLangParser.IF)
            self.state = 72
            self.match(WhileLangParser.LPAREN)
            self.state = 73
            self.expr(0)
            self.state = 74
            self.match(WhileLangParser.RPAREN)
            self.state = 75
            self.block()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 76
                self.match(WhileLangParser.ELSE)
                self.state = 77
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(WhileLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(WhileLangParser.BlockContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = WhileLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(WhileLangParser.WHILE)
            self.state = 81
            self.match(WhileLangParser.LPAREN)
            self.state = 82
            self.expr(0)
            self.state = 83
            self.match(WhileLangParser.RPAREN)
            self.state = 84
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(WhileLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = WhileLangParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(WhileLangParser.BREAK)
            self.state = 87
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(WhileLangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = WhileLangParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(WhileLangParser.CONTINUE)
            self.state = 90
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(WhileLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(WhileLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)

        def LT(self):
            return self.getToken(WhileLangParser.LT, 0)
        def GT(self):
            return self.getToken(WhileLangParser.GT, 0)
        def GE(self):
            return self.getToken(WhileLangParser.GE, 0)
        def LE(self):
            return self.getToken(WhileLangParser.LE, 0)
        def EQ(self):
            return self.getToken(WhileLangParser.EQ, 0)
        def NE(self):
            return self.getToken(WhileLangParser.NE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(WhileLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(WhileLangParser.MINUS, 0)
        def MUL(self):
            return self.getToken(WhileLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(WhileLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpr" ):
                listener.enterArithmeticExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpr" ):
                listener.exitArithmeticExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpr" ):
                return visitor.visitArithmeticExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = WhileLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 93
                self.match(WhileLangParser.ID)
                pass
            elif token in [25]:
                localctx = WhileLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                self.match(WhileLangParser.NUMBER)
                pass
            elif token in [26]:
                localctx = WhileLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(WhileLangParser.STRING)
                pass
            elif token in [8]:
                localctx = WhileLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.match(WhileLangParser.LPAREN)
                self.state = 97
                self.expr(0)
                self.state = 98
                self.match(WhileLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 108
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = WhileLangParser.ComparisonExprContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 103
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 104
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = WhileLangParser.ArithmeticExprContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 106
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 107
                        self.expr(3)
                        pass

             
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




