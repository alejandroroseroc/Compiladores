from antlr4 import *
from generated.WhileLangLexer import WhileLangLexer
from generated.WhileLangParser import WhileLangParser
from antlr4.Token import Token
from antlr4.tree.Tree import TerminalNode

input_text = """int a = 10;
while (a < 20) {
  if (a == 5) {
    break;
  }
  a = a + 1;
  continue;
}
"""

input_stream = InputStream(input_text)
lexer = WhileLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## TOKENS")
for token in token_stream.tokens:
    if token.type != Token.EOF:
        print(f"- {lexer.symbolicNames[token.type]} ('{token.text}') @ {token.line}:{token.column}")

parser = WhileLangParser(token_stream)
tree = parser.program()
print("\n## toStringTree:")
print(tree.toStringTree(recog=parser))

def pretty(node, rule_names, level=0):
    if isinstance(node, TerminalNode):
        return "  "*level + f"TOKEN({node.getText()})"
    name = rule_names[node.getRuleIndex()]
    s = "  "*level + name
    for c in node.children or []:
        s += "\n" + pretty(c, rule_names, level+1)
    return s

print("\n## Árbol (indentado):")
print(pretty(tree, parser.ruleNames))
