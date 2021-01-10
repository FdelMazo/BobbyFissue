import re
import sys

board = sys.stdin.read()
board = re.sub(r"([rRnNbBqQkKpP])", rf"![](https://raw.githubusercontent.com/FdelMazo/BobbyFissue/master/pieces/\1.png)", board)

print(board)
