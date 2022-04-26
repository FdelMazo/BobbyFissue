import re
import sys

wholeboard = sys.stdin.read()
header, board = wholeboard.split('**8**')
board = re.sub(r"([rRnNbBqQkKpP])", rf"![](https://raw.githubusercontent.com/FdelMazo/BobbyFissue/master/pieces/\1.png)", board)
board = re.sub(r" ", rf"![](https://raw.githubusercontent.com/FdelMazo/BobbyFissue/master/pieces/empty.png)", board)
result = '**8**'.join([header, board])

print(result)
