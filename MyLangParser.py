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
        4,1,39,282,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,4,0,40,8,0,
        11,0,12,0,41,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,5,5,77,8,5,10,5,12,5,80,9,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,5,5,89,8,5,10,5,12,5,92,9,5,1,5,1,5,5,5,96,8,5,10,5,
        12,5,99,9,5,1,5,1,5,1,5,5,5,104,8,5,10,5,12,5,107,9,5,1,5,3,5,110,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,120,8,6,11,6,12,6,121,5,
        6,124,8,6,10,6,12,6,127,9,6,1,6,1,6,4,6,131,8,6,11,6,12,6,132,3,
        6,135,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,148,8,
        7,10,7,12,7,151,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,5,8,165,8,8,10,8,12,8,168,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,5,9,178,8,9,10,9,12,9,181,9,9,1,9,1,9,1,10,1,10,1,10,5,10,188,
        8,10,10,10,12,10,191,9,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
        5,11,201,8,11,10,11,12,11,204,9,11,1,12,1,12,5,12,208,8,12,10,12,
        12,12,211,9,12,1,12,1,12,1,13,1,13,1,13,1,13,3,13,219,8,13,1,14,
        1,14,1,14,1,14,5,14,225,8,14,10,14,12,14,228,9,14,1,14,1,14,1,15,
        1,15,1,15,1,15,5,15,236,8,15,10,15,12,15,239,9,15,3,15,241,8,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,254,
        8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,3,18,269,8,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,277,8,18,10,
        18,12,18,280,9,18,1,18,0,1,36,19,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,0,0,300,0,39,1,0,0,0,2,52,1,0,0,0,4,54,1,0,
        0,0,6,59,1,0,0,0,8,62,1,0,0,0,10,70,1,0,0,0,12,111,1,0,0,0,14,139,
        1,0,0,0,16,154,1,0,0,0,18,171,1,0,0,0,20,184,1,0,0,0,22,198,1,0,
        0,0,24,205,1,0,0,0,26,218,1,0,0,0,28,220,1,0,0,0,30,231,1,0,0,0,
        32,244,1,0,0,0,34,253,1,0,0,0,36,268,1,0,0,0,38,40,3,2,1,0,39,38,
        1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,1,1,0,0,0,43,
        53,3,4,2,0,44,53,3,6,3,0,45,53,3,8,4,0,46,53,3,10,5,0,47,53,3,14,
        7,0,48,53,3,16,8,0,49,53,3,18,9,0,50,53,3,20,10,0,51,53,5,30,0,0,
        52,43,1,0,0,0,52,44,1,0,0,0,52,45,1,0,0,0,52,46,1,0,0,0,52,47,1,
        0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,
        3,1,0,0,0,54,55,5,20,0,0,55,56,5,36,0,0,56,57,5,1,0,0,57,58,3,36,
        18,0,58,5,1,0,0,0,59,60,5,22,0,0,60,61,3,36,18,0,61,7,1,0,0,0,62,
        63,5,19,0,0,63,64,5,2,0,0,64,65,3,34,17,0,65,66,5,3,0,0,66,67,5,
        4,0,0,67,68,6,4,-1,0,68,69,5,5,0,0,69,9,1,0,0,0,70,71,5,24,0,0,71,
        72,5,2,0,0,72,73,3,34,17,0,73,74,5,3,0,0,74,78,5,4,0,0,75,77,3,2,
        1,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,
        1,0,0,0,80,78,1,0,0,0,81,97,5,5,0,0,82,83,5,21,0,0,83,84,5,2,0,0,
        84,85,3,34,17,0,85,86,5,3,0,0,86,90,5,4,0,0,87,89,3,2,1,0,88,87,
        1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,
        92,90,1,0,0,0,93,94,5,5,0,0,94,96,1,0,0,0,95,82,1,0,0,0,96,99,1,
        0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,109,1,0,0,0,99,97,1,0,0,0,100,
        101,5,25,0,0,101,105,5,4,0,0,102,104,3,2,1,0,103,102,1,0,0,0,104,
        107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,
        105,1,0,0,0,108,110,5,5,0,0,109,100,1,0,0,0,109,110,1,0,0,0,110,
        11,1,0,0,0,111,112,5,26,0,0,112,113,5,2,0,0,113,114,3,36,18,0,114,
        115,5,3,0,0,115,125,5,4,0,0,116,117,5,27,0,0,117,119,5,37,0,0,118,
        120,3,2,1,0,119,118,1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,
        122,1,0,0,0,122,124,1,0,0,0,123,116,1,0,0,0,124,127,1,0,0,0,125,
        123,1,0,0,0,125,126,1,0,0,0,126,134,1,0,0,0,127,125,1,0,0,0,128,
        130,5,28,0,0,129,131,3,2,1,0,130,129,1,0,0,0,131,132,1,0,0,0,132,
        130,1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,128,1,0,0,0,134,
        135,1,0,0,0,135,136,1,0,0,0,136,137,5,5,0,0,137,138,5,29,0,0,138,
        13,1,0,0,0,139,140,5,6,0,0,140,141,5,2,0,0,141,142,5,36,0,0,142,
        143,5,7,0,0,143,144,3,26,13,0,144,145,5,3,0,0,145,149,5,4,0,0,146,
        148,3,2,1,0,147,146,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,
        150,1,0,0,0,150,152,1,0,0,0,151,149,1,0,0,0,152,153,5,5,0,0,153,
        15,1,0,0,0,154,155,5,6,0,0,155,156,5,2,0,0,156,157,5,36,0,0,157,
        158,5,8,0,0,158,159,5,34,0,0,159,160,5,9,0,0,160,161,5,34,0,0,161,
        162,5,3,0,0,162,166,5,4,0,0,163,165,3,2,1,0,164,163,1,0,0,0,165,
        168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,
        166,1,0,0,0,169,170,5,5,0,0,170,17,1,0,0,0,171,172,5,10,0,0,172,
        173,5,2,0,0,173,174,3,34,17,0,174,175,5,3,0,0,175,179,5,4,0,0,176,
        178,3,2,1,0,177,176,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,
        180,1,0,0,0,180,182,1,0,0,0,181,179,1,0,0,0,182,183,5,5,0,0,183,
        19,1,0,0,0,184,185,5,11,0,0,185,189,5,4,0,0,186,188,3,2,1,0,187,
        186,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,
        192,1,0,0,0,191,189,1,0,0,0,192,193,5,5,0,0,193,194,5,19,0,0,194,
        195,5,2,0,0,195,196,3,34,17,0,196,197,5,3,0,0,197,21,1,0,0,0,198,
        202,5,12,0,0,199,201,5,35,0,0,200,199,1,0,0,0,201,204,1,0,0,0,202,
        200,1,0,0,0,202,203,1,0,0,0,203,23,1,0,0,0,204,202,1,0,0,0,205,209,
        5,13,0,0,206,208,5,35,0,0,207,206,1,0,0,0,208,211,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,209,1,0,0,0,212,213,
        5,13,0,0,213,25,1,0,0,0,214,219,3,28,14,0,215,219,3,30,15,0,216,
        219,5,36,0,0,217,219,5,34,0,0,218,214,1,0,0,0,218,215,1,0,0,0,218,
        216,1,0,0,0,218,217,1,0,0,0,219,27,1,0,0,0,220,221,5,14,0,0,221,
        226,3,36,18,0,222,223,5,15,0,0,223,225,3,36,18,0,224,222,1,0,0,0,
        225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,229,1,0,0,0,
        228,226,1,0,0,0,229,230,5,16,0,0,230,29,1,0,0,0,231,240,5,4,0,0,
        232,237,3,32,16,0,233,234,5,15,0,0,234,236,3,32,16,0,235,233,1,0,
        0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,241,1,0,
        0,0,239,237,1,0,0,0,240,232,1,0,0,0,240,241,1,0,0,0,241,242,1,0,
        0,0,242,243,5,5,0,0,243,31,1,0,0,0,244,245,5,35,0,0,245,246,5,17,
        0,0,246,247,3,36,18,0,247,33,1,0,0,0,248,249,3,36,18,0,249,250,5,
        32,0,0,250,251,3,36,18,0,251,254,1,0,0,0,252,254,5,33,0,0,253,248,
        1,0,0,0,253,252,1,0,0,0,254,35,1,0,0,0,255,256,6,18,-1,0,256,269,
        5,34,0,0,257,269,5,35,0,0,258,269,5,36,0,0,259,269,5,33,0,0,260,
        269,3,28,14,0,261,269,3,30,15,0,262,263,5,2,0,0,263,264,3,36,18,
        0,264,265,5,31,0,0,265,266,3,36,18,0,266,267,5,3,0,0,267,269,1,0,
        0,0,268,255,1,0,0,0,268,257,1,0,0,0,268,258,1,0,0,0,268,259,1,0,
        0,0,268,260,1,0,0,0,268,261,1,0,0,0,268,262,1,0,0,0,269,278,1,0,
        0,0,270,271,10,1,0,0,271,272,5,18,0,0,272,273,3,36,18,0,273,274,
        5,17,0,0,274,275,3,36,18,2,275,277,1,0,0,0,276,270,1,0,0,0,277,280,
        1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,37,1,0,0,0,280,278,1,
        0,0,0,24,41,52,78,90,97,105,109,121,125,132,134,149,166,179,189,
        202,209,218,226,237,240,253,268,278
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'{'", "'}'", "'for'", 
                     "'in'", "'from'", "'to'", "'unless'", "'do'", "'//'", 
                     "'///'", "'['", "','", "']'", "':'", "'?'", "'while'", 
                     "'let'", "'else if'", "'print'", "'return'", "'if'", 
                     "'else'", "'switch'", "'case'", "'default'", "'end switch'", 
                     "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WHILE", "LET", 
                      "ELIF", "PRINT", "RETURN", "IF", "ELSE", "SWITCH", 
                      "CASE", "DEFAULT", "END_SWITCH", "PASS", "OPERATOR", 
                      "COMPARISON_OP", "BOOLEAN", "INT", "STRING", "ID", 
                      "LITERAL", "WS", "NEWLINE" ]

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
    RULE_doWhileStatement = 10
    RULE_comment = 11
    RULE_multilineComment = 12
    RULE_iterable = 13
    RULE_array = 14
    RULE_object = 15
    RULE_pair = 16
    RULE_condition = 17
    RULE_expression = 18

    ruleNames =  [ "program", "statement", "variableDeclaration", "printStatement", 
                   "whileStatement", "ifElseStatement", "switchStatement", 
                   "forEachStatement", "forRangeStatement", "unlessStatement", 
                   "doWhileStatement", "comment", "multilineComment", "iterable", 
                   "array", "object", "pair", "condition", "expression" ]

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
    T__17=18
    WHILE=19
    LET=20
    ELIF=21
    PRINT=22
    RETURN=23
    IF=24
    ELSE=25
    SWITCH=26
    CASE=27
    DEFAULT=28
    END_SWITCH=29
    PASS=30
    OPERATOR=31
    COMPARISON_OP=32
    BOOLEAN=33
    INT=34
    STRING=35
    ID=36
    LITERAL=37
    WS=38
    NEWLINE=39

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
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.statement()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0)):
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


        def doWhileStatement(self):
            return self.getTypedRuleContext(MyLangParser.DoWhileStatementContext,0)


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
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.whileStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.ifElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.forEachStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.forRangeStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.unlessStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 50
                self.doWhileStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 51
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
            self.state = 54
            self.match(MyLangParser.LET)
            self.state = 55
            self.match(MyLangParser.ID)
            self.state = 56
            self.match(MyLangParser.T__0)
            self.state = 57
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
            self.state = 59
            self.match(MyLangParser.PRINT)
            self.state = 60
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
            self.state = 62
            self.match(MyLangParser.WHILE)
            self.state = 63
            self.match(MyLangParser.T__1)
            self.state = 64
            self.condition()
            self.state = 65
            self.match(MyLangParser.T__2)
            self.state = 66
            self.match(MyLangParser.T__3)
            statement
            self.state = 68
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
            self.state = 70
            self.match(MyLangParser.IF)
            self.state = 71
            self.match(MyLangParser.T__1)
            self.state = 72
            self.condition()
            self.state = 73
            self.match(MyLangParser.T__2)
            self.state = 74
            self.match(MyLangParser.T__3)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0):
                self.state = 75
                self.statement()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(MyLangParser.T__4)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 82
                self.match(MyLangParser.ELIF)
                self.state = 83
                self.match(MyLangParser.T__1)
                self.state = 84
                self.condition()
                self.state = 85
                self.match(MyLangParser.T__2)
                self.state = 86
                self.match(MyLangParser.T__3)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0):
                    self.state = 87
                    self.statement()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 93
                self.match(MyLangParser.T__4)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 100
                self.match(MyLangParser.ELSE)
                self.state = 101
                self.match(MyLangParser.T__3)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0):
                    self.state = 102
                    self.statement()
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 108
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
            self.state = 111
            self.match(MyLangParser.SWITCH)
            self.state = 112
            self.match(MyLangParser.T__1)
            self.state = 113
            self.expression(0)
            self.state = 114
            self.match(MyLangParser.T__2)
            self.state = 115
            self.match(MyLangParser.T__3)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 116
                self.match(MyLangParser.CASE)
                self.state = 117
                self.match(MyLangParser.LITERAL)
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 118
                    self.statement()
                    self.state = 121 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0)):
                        break

                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 128
                self.match(MyLangParser.DEFAULT)
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 129
                    self.statement()
                    self.state = 132 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0)):
                        break



            self.state = 136
            self.match(MyLangParser.T__4)
            self.state = 137
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
            self.state = 139
            self.match(MyLangParser.T__5)
            self.state = 140
            self.match(MyLangParser.T__1)
            self.state = 141
            self.match(MyLangParser.ID)
            self.state = 142
            self.match(MyLangParser.T__6)
            self.state = 143
            self.iterable()
            self.state = 144
            self.match(MyLangParser.T__2)
            self.state = 145
            self.match(MyLangParser.T__3)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0):
                self.state = 146
                self.statement()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
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
            self.state = 154
            self.match(MyLangParser.T__5)
            self.state = 155
            self.match(MyLangParser.T__1)
            self.state = 156
            self.match(MyLangParser.ID)
            self.state = 157
            self.match(MyLangParser.T__7)
            self.state = 158
            self.match(MyLangParser.INT)
            self.state = 159
            self.match(MyLangParser.T__8)
            self.state = 160
            self.match(MyLangParser.INT)
            self.state = 161
            self.match(MyLangParser.T__2)
            self.state = 162
            self.match(MyLangParser.T__3)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0):
                self.state = 163
                self.statement()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
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
            self.state = 171
            self.match(MyLangParser.T__9)
            self.state = 172
            self.match(MyLangParser.T__1)
            self.state = 173
            self.condition()
            self.state = 174
            self.match(MyLangParser.T__2)
            self.state = 175
            self.match(MyLangParser.T__3)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0):
                self.state = 176
                self.statement()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(MyLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyLangParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(MyLangParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = MyLangParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_doWhileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MyLangParser.T__10)
            self.state = 185
            self.match(MyLangParser.T__3)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1096289344) != 0):
                self.state = 186
                self.statement()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
            self.match(MyLangParser.T__4)
            self.state = 193
            self.match(MyLangParser.WHILE)
            self.state = 194
            self.match(MyLangParser.T__1)
            self.state = 195
            self.condition()
            self.state = 196
            self.match(MyLangParser.T__2)
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
        self.enterRule(localctx, 22, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MyLangParser.T__11)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 199
                self.match(MyLangParser.STRING)
                self.state = 204
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
        self.enterRule(localctx, 24, self.RULE_multilineComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MyLangParser.T__12)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 206
                self.match(MyLangParser.STRING)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(MyLangParser.T__12)
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
        self.enterRule(localctx, 26, self.RULE_iterable)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.array()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.object_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.match(MyLangParser.ID)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
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
        self.enterRule(localctx, 28, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MyLangParser.T__13)
            self.state = 221
            self.expression(0)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 222
                self.match(MyLangParser.T__14)
                self.state = 223
                self.expression(0)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
            self.match(MyLangParser.T__15)
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
        self.enterRule(localctx, 30, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MyLangParser.T__3)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 232
                self.pair()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 233
                    self.match(MyLangParser.T__14)
                    self.state = 234
                    self.pair()
                    self.state = 239
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 242
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
        self.enterRule(localctx, 32, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MyLangParser.STRING)
            self.state = 245
            self.match(MyLangParser.T__16)
            self.state = 246
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
        self.enterRule(localctx, 34, self.RULE_condition)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.expression(0)
                self.state = 249
                self.match(MyLangParser.COMPARISON_OP)
                self.state = 250
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 256
                self.match(MyLangParser.INT)
                pass
            elif token in [35]:
                self.state = 257
                self.match(MyLangParser.STRING)
                pass
            elif token in [36]:
                self.state = 258
                self.match(MyLangParser.ID)
                pass
            elif token in [33]:
                self.state = 259
                self.match(MyLangParser.BOOLEAN)
                pass
            elif token in [14]:
                self.state = 260
                self.array()
                pass
            elif token in [4]:
                self.state = 261
                self.object_()
                pass
            elif token in [2]:
                self.state = 262
                self.match(MyLangParser.T__1)
                self.state = 263
                self.expression(0)
                self.state = 264
                self.match(MyLangParser.OPERATOR)
                self.state = 265
                self.expression(0)
                self.state = 266
                self.match(MyLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 270
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 271
                    self.match(MyLangParser.T__17)
                    self.state = 272
                    self.expression(0)
                    self.state = 273
                    self.match(MyLangParser.T__16)
                    self.state = 274
                    self.expression(2) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self._predicates[18] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




