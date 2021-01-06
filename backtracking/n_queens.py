# https://leetcode.com/problems/n-queens/

board = []
def solveNQueens(n: int):
  put_queen_on_board(n, 0, [])
  return board

def put_queen_on_board(n, row, current_board: list):
  if row >= n:
    board.append(current_board.copy())
    return

  for col in range(n):
    if has_alignment_queen(n, current_board, row, col):
      continue
    board_row = build_next_row(n, col)
    current_board.append(board_row)
    put_queen_on_board(n, row + 1, current_board)
    current_board.pop()

def has_alignment_queen(n, current_board, row, col):
  has_other_queen = False
  difference = 0
  for prev_row in range(row - 1, -1, -1):
    has_other_queen |= True if current_board[prev_row][col] == 'Q' else False
    difference += 1
    if is_in_board(n, col - difference):
      has_other_queen |= True if current_board[prev_row][col - difference] == 'Q' else False
    if is_in_board(n, col + difference):
      has_other_queen |= True if current_board[prev_row][col + difference] == 'Q' else False
    if has_other_queen:
      break
  return has_other_queen

def is_in_board(n, index):
  return 0 <= index and index < n

def build_next_row(col_length, queen_index):
  board_row = ''
  for i in range(col_length):
    board_row += '.' if i != queen_index else "Q"
  return board_row

print(solveNQueens(4))