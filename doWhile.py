from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from antlr4.tree.Tree import ParseTreeWalker

def main():
    # Test case for do-while loop
    expression = """
let x = 2
do {
    print x
    let x = (x + 1)
} while (x < 5)
"""
    # Create an input stream from the expression
    input_stream = InputStream(expression)

    # Lexical and syntactical analysis
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)

    # Parse the input into a tree
    tree = parser.program()

    # Initialize the evaluator
    evaluator = Evaluator()

    # Walk the parse tree using the evaluator
    walker = ParseTreeWalker()
    walker.walk(evaluator, tree)

if __name__ == "__main__":
    main()
