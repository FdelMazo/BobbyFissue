import sys
import chess

fen = sys.argv[1]
move = sys.argv[2]

board = chess.Board(fen)
board.push_san(move)
res = board.fen()

if board.is_checkmate():
	res = f"{res} +"
elif board.is_stalemate() or board.is_insufficient_material():
	res = f"{res} -"

print(board.fen())
