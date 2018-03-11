board = [[0]*6 for i in range(6)]
# obstacles
board[2][3]='#'
board[3][2]='#'
board[3][4]='#'
board[4][3]='#'
# final state
board[2][4]='$'
# start state
board[4][1]='@'


# -1 reward for any move
# movement will be only up,down, left and right
# 10 reward for reaching the final state
q = [[0]*6 for i in range(6)]









print(board)