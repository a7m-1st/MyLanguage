import pytest
from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from io import StringIO
import sys
from antlr4.tree.Tree import ParseTreeWalker

def execute_expression(expression: str) -> str:
   input_stream = InputStream(expression)
   lexer = MyLangLexer(input_stream)
   token_stream = CommonTokenStream(lexer)
   parser = MyLangParser(token_stream)
   tree = parser.program()
   evaluator = Evaluator()

   captured_output = StringIO()
   sys.stdout = captured_output  
   walker = ParseTreeWalker()
   walker.walk(evaluator, tree)

   sys.stdout = sys.__stdout__  
   return captured_output.getvalue().strip()


# Test case 1: Simple ascending for loop
def test_for_loop_ascending():
   expression = """
   for (5) {
       print "Hello"
   }
   """
   expected_output = "Entering a for loop...\nHello\nHello\nHello\nHello"
   output = execute_expression(expression)
   assert output == expected_output, f"Output: {output}, Expected: {expected_output}"

if __name__ == "__main__":
   pytest.main()