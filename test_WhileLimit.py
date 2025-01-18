import pytest
from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from io import StringIO
import sys

def execute_expression(expression: str) -> str:
    input_stream = InputStream(expression)

    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)
    tree = parser.program()  
    calc_evaluator = Evaluator()

    captured_output = StringIO()
    sys.stdout = captured_output  
    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)

    sys.stdout = sys.__stdout__  

    return captured_output.getvalue()


def test_while_limit():
    expression = """
    while (true limit 3) {
        print "Hello"
    }
    """
    output = execute_expression(expression)
    assert output == "Hello\nHello\nHello\n"