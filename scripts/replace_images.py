import re
import sys

board = sys.argv[1]
board = re.sub(r"([rRnNbBqQkKpP])", rf"![](https://raw.githubusercontent.com/FdelMazo/BobbyFissue/master/pieces/\1.png)", board)

print(board)
