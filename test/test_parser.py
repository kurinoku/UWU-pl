import common
from tokenizer import Tokenizer
from uwu_parser import Parser

script = """
O.O @_@
:v @_@ 2
UwU @_@
"""

tkn = Tokenizer.from_string(script)
p = Parser(tkn)
print(p.parse())

