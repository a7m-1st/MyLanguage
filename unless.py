from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from antlr4.tree.Tree import ParseTreeWalker

def main():
    # Simplified test case for debugging
    expression = """
let x = 10
unless (x > 20) {
    print "x is not greater than 20"
    let x = (x + 5)
}
"""

    input_stream = InputStream(expression)

    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)

    tree = parser.program()

    evaluator = Evaluator()
    walker = ParseTreeWalker()
    walker.walk(evaluator, tree)

if __name__ == "__main__":
    main()
