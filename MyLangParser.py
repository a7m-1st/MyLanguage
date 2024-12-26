# Generated from MyLang.g4 by ANTLR 4.13.2
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
        4,1,38,265,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,5,5,74,8,5,10,5,12,5,77,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,
        5,86,8,5,10,5,12,5,89,9,5,1,5,1,5,5,5,93,8,5,10,5,12,5,96,9,5,1,
        5,1,5,1,5,5,5,101,8,5,10,5,12,5,104,9,5,1,5,3,5,107,8,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,4,6,117,8,6,11,6,12,6,118,5,6,121,8,6,10,
        6,12,6,124,9,6,1,6,1,6,4,6,128,8,6,11,6,12,6,129,3,6,132,8,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,145,8,7,10,7,12,7,148,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,162,8,8,
        10,8,12,8,165,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,175,8,9,10,
        9,12,9,178,9,9,1,9,1,9,1,10,1,10,5,10,184,8,10,10,10,12,10,187,9,
        10,1,11,1,11,5,11,191,8,11,10,11,12,11,194,9,11,1,11,1,11,1,12,1,
        12,1,12,1,12,3,12,202,8,12,1,13,1,13,1,13,1,13,5,13,208,8,13,10,
        13,12,13,211,9,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,219,8,14,10,
        14,12,14,222,9,14,3,14,224,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        16,1,16,1,16,1,16,1,16,3,16,237,8,16,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,252,8,17,1,17,1,17,1,
        17,1,17,1,17,1,17,5,17,260,8,17,10,17,12,17,263,9,17,1,17,0,1,34,
        18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,0,282,0,37,
        1,0,0,0,2,49,1,0,0,0,4,51,1,0,0,0,6,56,1,0,0,0,8,59,1,0,0,0,10,67,
        1,0,0,0,12,108,1,0,0,0,14,136,1,0,0,0,16,151,1,0,0,0,18,168,1,0,
        0,0,20,181,1,0,0,0,22,188,1,0,0,0,24,201,1,0,0,0,26,203,1,0,0,0,
        28,214,1,0,0,0,30,227,1,0,0,0,32,236,1,0,0,0,34,251,1,0,0,0,36,38,
        3,2,1,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,
        40,1,1,0,0,0,41,50,3,4,2,0,42,50,3,6,3,0,43,50,3,8,4,0,44,50,3,10,
        5,0,45,50,3,14,7,0,46,50,3,16,8,0,47,50,3,18,9,0,48,50,5,29,0,0,
        49,41,1,0,0,0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,
        0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,3,1,0,0,0,51,
        52,5,19,0,0,52,53,5,35,0,0,53,54,5,1,0,0,54,55,3,34,17,0,55,5,1,
        0,0,0,56,57,5,21,0,0,57,58,3,34,17,0,58,7,1,0,0,0,59,60,5,18,0,0,
        60,61,5,2,0,0,61,62,3,32,16,0,62,63,5,3,0,0,63,64,5,4,0,0,64,65,
        6,4,-1,0,65,66,5,5,0,0,66,9,1,0,0,0,67,68,5,23,0,0,68,69,5,2,0,0,
        69,70,3,32,16,0,70,71,5,3,0,0,71,75,5,4,0,0,72,74,3,2,1,0,73,72,
        1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,
        77,75,1,0,0,0,78,94,5,5,0,0,79,80,5,20,0,0,80,81,5,2,0,0,81,82,3,
        32,16,0,82,83,5,3,0,0,83,87,5,4,0,0,84,86,3,2,1,0,85,84,1,0,0,0,
        86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,
        0,0,0,90,91,5,5,0,0,91,93,1,0,0,0,92,79,1,0,0,0,93,96,1,0,0,0,94,
        92,1,0,0,0,94,95,1,0,0,0,95,106,1,0,0,0,96,94,1,0,0,0,97,98,5,24,
        0,0,98,102,5,4,0,0,99,101,3,2,1,0,100,99,1,0,0,0,101,104,1,0,0,0,
        102,100,1,0,0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,
        105,107,5,5,0,0,106,97,1,0,0,0,106,107,1,0,0,0,107,11,1,0,0,0,108,
        109,5,25,0,0,109,110,5,2,0,0,110,111,3,34,17,0,111,112,5,3,0,0,112,
        122,5,4,0,0,113,114,5,26,0,0,114,116,5,36,0,0,115,117,3,2,1,0,116,
        115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,
        121,1,0,0,0,120,113,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,
        123,1,0,0,0,123,131,1,0,0,0,124,122,1,0,0,0,125,127,5,27,0,0,126,
        128,3,2,1,0,127,126,1,0,0,0,128,129,1,0,0,0,129,127,1,0,0,0,129,
        130,1,0,0,0,130,132,1,0,0,0,131,125,1,0,0,0,131,132,1,0,0,0,132,
        133,1,0,0,0,133,134,5,5,0,0,134,135,5,28,0,0,135,13,1,0,0,0,136,
        137,5,6,0,0,137,138,5,2,0,0,138,139,5,35,0,0,139,140,5,7,0,0,140,
        141,3,24,12,0,141,142,5,3,0,0,142,146,5,4,0,0,143,145,3,2,1,0,144,
        143,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,
        149,1,0,0,0,148,146,1,0,0,0,149,150,5,5,0,0,150,15,1,0,0,0,151,152,
        5,6,0,0,152,153,5,2,0,0,153,154,5,35,0,0,154,155,5,8,0,0,155,156,
        5,33,0,0,156,157,5,9,0,0,157,158,5,33,0,0,158,159,5,3,0,0,159,163,
        5,4,0,0,160,162,3,2,1,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,
        1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,167,
        5,5,0,0,167,17,1,0,0,0,168,169,5,10,0,0,169,170,5,2,0,0,170,171,
        3,32,16,0,171,172,5,3,0,0,172,176,5,4,0,0,173,175,3,2,1,0,174,173,
        1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,179,
        1,0,0,0,178,176,1,0,0,0,179,180,5,5,0,0,180,19,1,0,0,0,181,185,5,
        11,0,0,182,184,5,34,0,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,
        1,0,0,0,185,186,1,0,0,0,186,21,1,0,0,0,187,185,1,0,0,0,188,192,5,
        12,0,0,189,191,5,34,0,0,190,189,1,0,0,0,191,194,1,0,0,0,192,190,
        1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,192,1,0,0,0,195,196,
        5,12,0,0,196,23,1,0,0,0,197,202,3,26,13,0,198,202,3,28,14,0,199,
        202,5,35,0,0,200,202,5,33,0,0,201,197,1,0,0,0,201,198,1,0,0,0,201,
        199,1,0,0,0,201,200,1,0,0,0,202,25,1,0,0,0,203,204,5,13,0,0,204,
        209,3,34,17,0,205,206,5,14,0,0,206,208,3,34,17,0,207,205,1,0,0,0,
        208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,
        211,209,1,0,0,0,212,213,5,15,0,0,213,27,1,0,0,0,214,223,5,4,0,0,
        215,220,3,30,15,0,216,217,5,14,0,0,217,219,3,30,15,0,218,216,1,0,
        0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,224,1,0,
        0,0,222,220,1,0,0,0,223,215,1,0,0,0,223,224,1,0,0,0,224,225,1,0,
        0,0,225,226,5,5,0,0,226,29,1,0,0,0,227,228,5,34,0,0,228,229,5,16,
        0,0,229,230,3,34,17,0,230,31,1,0,0,0,231,232,3,34,17,0,232,233,5,
        31,0,0,233,234,3,34,17,0,234,237,1,0,0,0,235,237,5,32,0,0,236,231,
        1,0,0,0,236,235,1,0,0,0,237,33,1,0,0,0,238,239,6,17,-1,0,239,252,
        5,33,0,0,240,252,5,34,0,0,241,252,5,35,0,0,242,252,5,32,0,0,243,
        252,3,26,13,0,244,252,3,28,14,0,245,246,5,2,0,0,246,247,3,34,17,
        0,247,248,5,30,0,0,248,249,3,34,17,0,249,250,5,3,0,0,250,252,1,0,
        0,0,251,238,1,0,0,0,251,240,1,0,0,0,251,241,1,0,0,0,251,242,1,0,
        0,0,251,243,1,0,0,0,251,244,1,0,0,0,251,245,1,0,0,0,252,261,1,0,
        0,0,253,254,10,1,0,0,254,255,5,17,0,0,255,256,3,34,17,0,256,257,
        5,16,0,0,257,258,3,34,17,2,258,260,1,0,0,0,259,253,1,0,0,0,260,263,
        1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,35,1,0,0,0,263,261,1,
        0,0,0,23,39,49,75,87,94,102,106,118,122,129,131,146,163,176,185,
        192,201,209,220,223,236,251,261
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'{'", "'}'", "'for'", 
                     "'in'", "'from'", "'to'", "'unless'", "'//'", "'///'", 
                     "'['", "','", "']'", "':'", "'?'", "'while'", "'let'", 
                     "'else if'", "'print'", "'return'", "'if'", "'else'", 
                     "'switch'", "'case'", "'default'", "'end switch'", 
                     "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WHILE", "LET", "ELIF", 
                      "PRINT", "RETURN", "IF", "ELSE", "SWITCH", "CASE", 
                      "DEFAULT", "END_SWITCH", "PASS", "OPERATOR", "COMPARISON_OP", 
                      "BOOLEAN", "INT", "STRING", "ID", "LITERAL", "WS", 
                      "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_printStatement = 3
    RULE_whileStatement = 4
    RULE_ifElseStatement = 5
    RULE_switchStatement = 6
    RULE_forEachStatement = 7
    RULE_forRangeStatement = 8
    RULE_unlessStatement = 9
    RULE_comment = 10
    RULE_multilineComment = 11
    RULE_iterable = 12
    RULE_array = 13
    RULE_object = 14
    RULE_pair = 15
    RULE_condition = 16
    RULE_expression = 17

    ruleNames =  [ "program", "statement", "variableDeclaration", "printStatement", 
                   "whileStatement", "ifElseStatement", "switchStatement", 
                   "forEachStatement", "forRangeStatement", "unlessStatement", 
                   "comment", "multilineComment", "iterable", "array", "object", 
                   "pair", "condition", "expression" ]

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
    T__15=16
    T__16=17
    WHILE=18
    LET=19
    ELIF=20
    PRINT=21
    RETURN=22
    IF=23
    ELSE=24
    SWITCH=25
    CASE=26
    DEFAULT=27
    END_SWITCH=28
    PASS=29
    OPERATOR=30
    COMPARISON_OP=31
    BOOLEAN=32
    INT=33
    STRING=34
    ID=35
    LITERAL=36
    WS=37
    NEWLINE=38

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0)):
                    break

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

        def variableDeclaration(self):
            return self.getTypedRuleContext(MyLangParser.VariableDeclarationContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(MyLangParser.PrintStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MyLangParser.WhileStatementContext,0)


        def ifElseStatement(self):
            return self.getTypedRuleContext(MyLangParser.IfElseStatementContext,0)


        def forEachStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForEachStatementContext,0)


        def forRangeStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForRangeStatementContext,0)


        def unlessStatement(self):
            return self.getTypedRuleContext(MyLangParser.UnlessStatementContext,0)


        def PASS(self):
            return self.getToken(MyLangParser.PASS, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.whileStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.ifElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.forEachStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.forRangeStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 47
                self.unlessStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 48
                self.match(MyLangParser.PASS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(MyLangParser.LET, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = MyLangParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MyLangParser.LET)
            self.state = 52
            self.match(MyLangParser.ID)
            self.state = 53
            self.match(MyLangParser.T__0)
            self.state = 54
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MyLangParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = MyLangParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MyLangParser.PRINT)
            self.state = 57
            self.expression(0)
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
            return self.getToken(MyLangParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(MyLangParser.ConditionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = MyLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(MyLangParser.WHILE)
            self.state = 60
            self.match(MyLangParser.T__1)
            self.state = 61
            self.condition()
            self.state = 62
            self.match(MyLangParser.T__2)
            self.state = 63
            self.match(MyLangParser.T__3)
            statement
            self.state = 65
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyLangParser.IF, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ConditionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.ELIF)
            else:
                return self.getToken(MyLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(MyLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_ifElseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseStatement" ):
                listener.enterIfElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseStatement" ):
                listener.exitIfElseStatement(self)




    def ifElseStatement(self):

        localctx = MyLangParser.IfElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifElseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(MyLangParser.IF)
            self.state = 68
            self.match(MyLangParser.T__1)
            self.state = 69
            self.condition()
            self.state = 70
            self.match(MyLangParser.T__2)
            self.state = 71
            self.match(MyLangParser.T__3)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0):
                self.state = 72
                self.statement()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(MyLangParser.T__4)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 79
                self.match(MyLangParser.ELIF)
                self.state = 80
                self.match(MyLangParser.T__1)
                self.state = 81
                self.condition()
                self.state = 82
                self.match(MyLangParser.T__2)
                self.state = 83
                self.match(MyLangParser.T__3)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0):
                    self.state = 84
                    self.statement()
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.match(MyLangParser.T__4)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 97
                self.match(MyLangParser.ELSE)
                self.state = 98
                self.match(MyLangParser.T__3)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0):
                    self.state = 99
                    self.statement()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 105
                self.match(MyLangParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(MyLangParser.SWITCH, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def END_SWITCH(self):
            return self.getToken(MyLangParser.END_SWITCH, 0)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.CASE)
            else:
                return self.getToken(MyLangParser.CASE, i)

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.LITERAL)
            else:
                return self.getToken(MyLangParser.LITERAL, i)

        def DEFAULT(self):
            return self.getToken(MyLangParser.DEFAULT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = MyLangParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MyLangParser.SWITCH)
            self.state = 109
            self.match(MyLangParser.T__1)
            self.state = 110
            self.expression(0)
            self.state = 111
            self.match(MyLangParser.T__2)
            self.state = 112
            self.match(MyLangParser.T__3)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 113
                self.match(MyLangParser.CASE)
                self.state = 114
                self.match(MyLangParser.LITERAL)
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 115
                    self.statement()
                    self.state = 118 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0)):
                        break

                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 125
                self.match(MyLangParser.DEFAULT)
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 126
                    self.statement()
                    self.state = 129 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0)):
                        break



            self.state = 133
            self.match(MyLangParser.T__4)
            self.state = 134
            self.match(MyLangParser.END_SWITCH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForEachStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def iterable(self):
            return self.getTypedRuleContext(MyLangParser.IterableContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_forEachStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForEachStatement" ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForEachStatement" ):
                listener.exitForEachStatement(self)




    def forEachStatement(self):

        localctx = MyLangParser.ForEachStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forEachStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MyLangParser.T__5)
            self.state = 137
            self.match(MyLangParser.T__1)
            self.state = 138
            self.match(MyLangParser.ID)
            self.state = 139
            self.match(MyLangParser.T__6)
            self.state = 140
            self.iterable()
            self.state = 141
            self.match(MyLangParser.T__2)
            self.state = 142
            self.match(MyLangParser.T__3)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0):
                self.state = 143
                self.statement()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.INT)
            else:
                return self.getToken(MyLangParser.INT, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_forRangeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForRangeStatement" ):
                listener.enterForRangeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForRangeStatement" ):
                listener.exitForRangeStatement(self)




    def forRangeStatement(self):

        localctx = MyLangParser.ForRangeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forRangeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MyLangParser.T__5)
            self.state = 152
            self.match(MyLangParser.T__1)
            self.state = 153
            self.match(MyLangParser.ID)
            self.state = 154
            self.match(MyLangParser.T__7)
            self.state = 155
            self.match(MyLangParser.INT)
            self.state = 156
            self.match(MyLangParser.T__8)
            self.state = 157
            self.match(MyLangParser.INT)
            self.state = 158
            self.match(MyLangParser.T__2)
            self.state = 159
            self.match(MyLangParser.T__3)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0):
                self.state = 160
                self.statement()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnlessStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(MyLangParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_unlessStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnlessStatement" ):
                listener.enterUnlessStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnlessStatement" ):
                listener.exitUnlessStatement(self)




    def unlessStatement(self):

        localctx = MyLangParser.UnlessStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unlessStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MyLangParser.T__9)
            self.state = 169
            self.match(MyLangParser.T__1)
            self.state = 170
            self.condition()
            self.state = 171
            self.match(MyLangParser.T__2)
            self.state = 172
            self.match(MyLangParser.T__3)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 548144192) != 0):
                self.state = 173
                self.statement()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.STRING)
            else:
                return self.getToken(MyLangParser.STRING, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = MyLangParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MyLangParser.T__10)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 182
                self.match(MyLangParser.STRING)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultilineCommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.STRING)
            else:
                return self.getToken(MyLangParser.STRING, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_multilineComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultilineComment" ):
                listener.enterMultilineComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultilineComment" ):
                listener.exitMultilineComment(self)




    def multilineComment(self):

        localctx = MyLangParser.MultilineCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_multilineComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MyLangParser.T__11)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 189
                self.match(MyLangParser.STRING)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(MyLangParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(MyLangParser.ArrayContext,0)


        def object_(self):
            return self.getTypedRuleContext(MyLangParser.ObjectContext,0)


        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = MyLangParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_iterable)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.array()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.object_()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(MyLangParser.ID)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.match(MyLangParser.INT)
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = MyLangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(MyLangParser.T__12)
            self.state = 204
            self.expression(0)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 205
                self.match(MyLangParser.T__13)
                self.state = 206
                self.expression(0)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(MyLangParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.PairContext)
            else:
                return self.getTypedRuleContext(MyLangParser.PairContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)




    def object_(self):

        localctx = MyLangParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MyLangParser.T__3)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 215
                self.pair()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 216
                    self.match(MyLangParser.T__13)
                    self.state = 217
                    self.pair()
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 225
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = MyLangParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MyLangParser.STRING)
            self.state = 228
            self.match(MyLangParser.T__15)
            self.state = 229
            self.expression(0)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def COMPARISON_OP(self):
            return self.getToken(MyLangParser.COMPARISON_OP, 0)

        def BOOLEAN(self):
            return self.getToken(MyLangParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = MyLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.expression(0)
                self.state = 232
                self.match(MyLangParser.COMPARISON_OP)
                self.state = 233
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(MyLangParser.BOOLEAN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def BOOLEAN(self):
            return self.getToken(MyLangParser.BOOLEAN, 0)

        def array(self):
            return self.getTypedRuleContext(MyLangParser.ArrayContext,0)


        def object_(self):
            return self.getTypedRuleContext(MyLangParser.ObjectContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def OPERATOR(self):
            return self.getToken(MyLangParser.OPERATOR, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 239
                self.match(MyLangParser.INT)
                pass
            elif token in [34]:
                self.state = 240
                self.match(MyLangParser.STRING)
                pass
            elif token in [35]:
                self.state = 241
                self.match(MyLangParser.ID)
                pass
            elif token in [32]:
                self.state = 242
                self.match(MyLangParser.BOOLEAN)
                pass
            elif token in [13]:
                self.state = 243
                self.array()
                pass
            elif token in [4]:
                self.state = 244
                self.object_()
                pass
            elif token in [2]:
                self.state = 245
                self.match(MyLangParser.T__1)
                self.state = 246
                self.expression(0)
                self.state = 247
                self.match(MyLangParser.OPERATOR)
                self.state = 248
                self.expression(0)
                self.state = 249
                self.match(MyLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 253
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 254
                    self.match(MyLangParser.T__16)
                    self.state = 255
                    self.expression(0)
                    self.state = 256
                    self.match(MyLangParser.T__15)
                    self.state = 257
                    self.expression(2) 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self._predicates[17] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




