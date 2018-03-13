class Game:

    state={}
    coordinate={}
    label=0
    for i in range(rows):
        for j in range(columns):
            state[(i,j)]=label
            coordinate[label]=(i,j)
            label+=1

    
    def __init__(self,rows,columns,start,end):
        self.board = [[0]*columns for i in range(rows)]
        self.board[2][3]='#'
        self.board[3][2]='#'
        self.board[3][4]='#'
        self.board[4][3]='#'

        # final state
        self.board[2][4]='$'
        # start state
        self.board[4][1]='@'
    

    def get_state(self,x,y):
        return state[(x,y)]

    def get_coordinate(self,s):
        return coordinate[state]





Board = Game(6,6,25,16)
print(Board.get_state(3,4))