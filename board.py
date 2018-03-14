class Board:

    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.board = [[0]*columns for i in range(rows)]
        self.board[2][3]='#'
        self.board[3][2]='#'
        self.board[3][4]='#'
        self.board[4][3]='#'
        # final state
        self.board[2][4]='$'
        self.final_state = 16
        # start state
        self.board[4][1]='@'
        self.start_state = 25

        self.state={}
        self.coordinate={}
        label=0
        for i in range(rows):
            for j in range(columns):
                self.state[(i,j)]=label
                self.coordinate[label]=(i,j)
                label+=1

        self.q={}
        for i in range(len(self.state)):
            self.q[i]=0
        self.q[16]=10

        self.visited = {}
        for i in range(len(self.state)):
            self.visited[i]=0
        self.visited[self.start_state]=1
        
    def display(self):
        for i in range(self.rows):
                temp = ' '.join(str(x) for x in self.board[i])
                print(temp)

    def get_state(self,x,y):
        return self.state[(x,y)]

    def get_coordinate(self,state):
        return self.coordinate[state]


    def is_safe(self,x,y):
    # print(x,y)
        if(x>=0 and y>=0 and x<self.columns and y<self.rows and self.board[x][y] != '#'):
            if(self.visited[self.get_state(x,y)] != 1):
                return True
        return False    

    def left(self,s):
        x,y = self.get_coordinate(s)
        return self.get_state(x,y-1)

    def right(self,s):
        x,y = self.get_coordinate(s)
        return self.get_state(x,y+1)

    def up(self,s):
        x,y = self.get_coordinate(s)
        return self.get_state(x-1,y)

    def down(self,s):
        x,y = self.get_coordinate(s)
        return self.get_state(x+1,y)


    


