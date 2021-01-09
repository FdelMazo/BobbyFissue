import re
import sys
import subprocess

# We receive the fen current position by CLA
# For example, an initial board would be called like this:
# python fen2md.py "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen = sys.argv[1]

# We take out any FEN 'metadata', we only care about the position, not the available castles/en passant/etc
fenPosition = fen.split()[0]

# We convert the fen position into a proto board, just delimited by the character |
# This function was taken from this codegolf https://codegolf.stackexchange.com/a/78340
def r(o): return ''.join(['| '*8if h=='8'else'| '*int(h)if h.isdigit()else'|\n'if h=='/'else'|'+h for h in o])+'|'

# We add some line numbers, using `nc`
# Yep, it's overkill to use a subprocess
cmd = f"""echo "{r(fenPosition)}" | tac | nl -w 1 -s '' | tac """
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
board = ps.communicate()[0].decode('utf-8')

# We want the line numbers to be bold in md
board = re.sub(r"(\d)", r"**\1**", board)

print(f"""
| |**A**|**B**|**C**|**D**|**E**|**F**|**G**|**H**|
|-|-|-|-|-|-|-|-|-|
{board}
""")
