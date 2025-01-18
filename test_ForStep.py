import pytest
from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from io import StringIO
import sys
from antlr4.tree.Tree import ParseTreeWalker


# Helper function to execute an expression and capture output
def execute_expression(expression: str) -> str:
   input_stream = InputStream(expression)
   lexer = MyLangLexer(input_stream)
   token_stream = CommonTokenStream(lexer)
   parser = MyLangParser(token_stream)
   tree = parser.program()


   evaluator = Evaluator()


   # Capture the output printed by the evaluator
   captured_output = StringIO()
   sys.stdout = captured_output  # Redirect stdout to capture print statements


   walker = ParseTreeWalker()
   walker.walk(evaluator, tree)


   sys.stdout = sys.__stdout__  # Reset stdout to normal
   return captured_output.getvalue().strip()


# Test case for ascending for-step loop
def test_for_step_ascending():
   expression = """
   for (1 to 5 step 1) {
       print loop
   }
   """
   expected_output = "1\n2\n3\n4\n5"
   output = execute_expression(expression)
   assert output == expected_output, f"Output: {output}, Expected: {expected_output}"


# Test case for descending for-step loop
def test_for_step_descending():
   expression = """
   for (5 to 1 step -1) {
       print loop
   }
   """
   expected_output = "5\n4\n3\n2\n1"
   output = execute_expression(expression)
   assert output == expected_output, f"Output: {output}, Expected: {expected_output}"


# Test case for step size that skips values
def test_for_step_skip_values():
   expression = """
   for (2 to 10 step 2) {
       print loop
   }
   """
   expected_output = "2\n4\n6\n8\n10"
   output = execute_expression(expression)
   assert output == expected_output, f"Output: {output}, Expected: {expected_output}"




if __name__ == "__main__":
   pytest.main()