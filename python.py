import chess
import datetime

import numpy as np


eval=[]

def bta(bb):
  return np.unpackbits((bb >> (8 * np.arange(7, -1, -1, dtype=np.uint64))).astype(np.uint8).reshape(-1, 8), axis=1, bitorder="little").ravel()
P=np.array([ 0,   0,   0,   0,   0,   0,   0,   0,
   78,  83,  86,  73, 102,  82,  85,  90,
   7,  29,  21,  44,  40,  31,  44,   7,
 -17,  16,  -2,  15,  14,   0,  15, -13,
 -26,   3,  10,   6,   9,   1,   0, -23,
 -22,   9,   5, -11, -10,  -2,   3, -19,
 -31,   8,  -7, -37, -36, -14,   3, -31,
   0,   0,   0,   0,  0,   0,   0,   0])+1000

N=np.array([ -66, -53, -75, -75, -10, -55, -58, -70,
  -3,  -6, 100, -36,   4,  62,  -4, -14,
  10,  67,   1,  74,  73,  27,  62,  -2,
  24,  24,  45,  37,  33,  41,  25,  17,
  -1,   5,  31,  21,  22,  35,   2,   0,
 -18,  10,  13,  22,  18,  15,  11, -14,
 -23, -15,   2,   0,   2,   0, -23, -20,
 -74, -23, -26, -24, -19, -35, -22, -69])+3000

B=np.array([-59, -78, -82, -76, -23,-107, -37, -50,
 -11,  20,  35, -42, -39,  31,   2, -22,
  -9,  39, -32,  41,  52, -10,  28, -14,
  25,  17,  20,  34,  26,  25,  15,  10,
  13,  10,  17,  23,  17,  16,   0,   7,
  14,  25,  24,  15,   8,  25,  20,  15,
  19,  20,  11,   6,   7,   6,  20,  16,
  -7,   2, -15, -12, -14, -15, -10, -10])+3200

R=np.array([35,  29,  33,   4,  37,  33,  56,  50,
  55,  29,  56,  67,  55,  62,  34,  60,
  19,  35,  28,  33,  45,  27,  25,  15,
   0,   5,  16,  13,  18,  -4,  -9,  -6,
 -28, -35, -16, -21, -13, -29, -46, -30,
 -42, -28, -42, -25, -25, -35, -26, -46,
 -53, -38, -31, -26, -29, -43, -44, -53,
 -30, -24, -18,   5,  -2, -18, -31, -32])+5000

Q=np.array([6,   1,  -8,-104,  69,  24,  88,  26,
  14,  32,  60, -10,  20,  76,  57,  24,
  -2,  43,  32,  60,  72,  63,  43,   2,
   1, -16,  22,  17,  25,  20, -13,  -22,
 -14, -15,  -2,  -5,  -1, -10, -20, -22,
 -30,  -6, -13, -11, -16, -11, -16, -27,
 -36, -18,   0, -19, -15, -15, -21, -38,
 -39, -30, -31, -13, -31, -36, -34, -42])+9000

K=np.array([4,  54,  47, -99, -99,  60,  83, -62,
 -32,  10,  55,  56,  56,  55,  10,   3,
 -62,  12, -57,  44, -67,  28,  37, -31,
 -55,  50,  11,  -4, -19,  13,   0, -49,
 -55, -43, -52, -28, -51, -47,  -8, -50,
 -47, -42, -43, -79, -64, -32, -29, -32,
  -4,   3, -14, -50, -57, -18,  13,   4,
  17,  30,  -3, -14,   6,  -1,  40,  18])

p=-np.flip(P)
n=-np.flip(N)
b=-np.flip(B)
r=-np.flip(R) 
q=-np.flip(Q)
k=-np.flip(K)

def ordereval(move):
  if board.gives_check(move):
    return 300
  if board.is_capture(move):
    return 200
  if board.is_castling(move):
    return 100
  return 50

def sort(arr):
    return sorted(arr, key=ordereval)



def evaluate(board,color):
  color=1 if color else -1
  if board.is_checkmate():
    return 205000*-color
  if board.is_stalemate():
    return 0
  if board.is_insufficient_material():
    return 0
  if board.is_fifty_moves():
    return 0
  if board.is_repetition(3):
    return 0
  eval = np.dot(bta(np.uint64(board.pieces(chess.PAWN, chess.WHITE))), P)
  eval += np.dot(bta(np.uint64(board.pieces(chess.KNIGHT, chess.WHITE))), N)
  eval += np.dot(bta(np.uint64(board.pieces(chess.BISHOP, chess.WHITE))), B)
  eval += np.dot(bta(np.uint64(board.pieces(chess.ROOK, chess.WHITE))), R)
  eval += np.dot(bta(np.uint64(board.pieces(chess.QUEEN, chess.WHITE))), Q)
  eval += np.dot(bta(np.uint64(board.pieces(chess.KING, chess.WHITE))), K)
  eval += np.dot(bta(np.uint64(board.pieces(chess.PAWN, chess.BLACK))), p)
  eval += np.dot(bta(np.uint64(board.pieces(chess.KNIGHT, chess.BLACK))), n)
  eval += np.dot(bta(np.uint64(board.pieces(chess.BISHOP, chess.BLACK))), b)
  eval += np.dot(bta(np.uint64(board.pieces(chess.ROOK, chess.BLACK))), r)
  eval += np.dot(bta(np.uint64(board.pieces(chess.QUEEN, chess.BLACK))), q)
  eval += np.dot(bta(np.uint64(board.pieces(chess.KING, chess.BLACK))), k)
  return eval



def minimax(board, depth, α, β, Maxplayer):
  if depth == 0 or not(bool(board.legal_moves)):
      return [evaluate(board,Maxplayer)]
  if Maxplayer:
      value = -10000000000
      maxnode=None
      for x in list(board.legal_moves):
        board_copy = board.copy()
        board_copy.push(x)
        value = max(value, minimax(board_copy, depth - 1, α, β, False)[0])
        if value > β:
            break 
        if value > α:
            α = value
            maxnode = x
      return [value,maxnode]
  else:
      value = 10000000000
      minnode = None
      for x in list(board.legal_moves):
        board_copy = board.copy()
        board_copy.push(x)
        value = min(value, minimax(board_copy, depth - 1, α, β, True)[0])
        if value < α:
            break 
        if value < β:
            β = value
            minnode = x
      return [value, minnode]


board=chess.Board('rnbqk2r/pppp1ppp/4pn2/3P4/1bP5/8/PP1BPPPP/RN1QKBNR b')


eval=[]
for depth in range(5):
  moves=list(board.legal_moves)
  moves=sort(moves)
  start=datetime.datetime.now()
  eval=minimax(board,depth,-100000000000,100000000000,False)
  print(datetime.datetime.now()-start)
  print(depth)
  print(eval)
  print()
