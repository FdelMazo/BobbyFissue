import sys
import chess

fen = sys.argv[1].strip()
move = sys.argv[2]

# Remove the 'custom fen' attribute (a last letter, I W or D which indicates InvalidMove, Win or Draw)
attrs = fen.split(' ')
if len(attrs) > 6:
	fen = ' '.join(attrs[:6])

board = chess.Board(fen)
invalid_move = False

try:
	board.push_san(move)
except ValueError:
	invalid_move = True

res = board.fen()

if invalid_move:
	res = f"{res} I"

if board.is_checkmate():
	res = f"{res} W"
elif board.is_stalemate() or board.is_insufficient_material():
	res = f"{res} D"

print(res)
