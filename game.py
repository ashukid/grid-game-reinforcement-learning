import random
import time


# board dimesions
m=6
n=6

board = [[0]*n for i in range(m)]
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
state={}
coordinate={}
label=0
for i in range(m):
    for j in range(n):
        state[(i,j)]=label
        coordinate[label]=(i,j)
        label+=1

def is_safe(coordinate):
    x,y=coordinate
    # print(x,y)
    if(x>=0 and y>=0 and x<n and y<m and board[x][y] != '#'):
        return True
    return False

def left(x,y):
    return (x-1,y)

def right(x,y):
    return (x+1,y)

def up(x,y):
    return (x,y-1)

def down(x,y):
    return (x,y+1)

def next_state(s,action):
    x,y=coordinate[s]
    if(action=='L'):
        newx,newy=left(x,y)
        return state[(newx,newy)]
    if(action=='R'):
        newx,newy=right(x,y)
        return state[(newx,newy)]
    if(action=='U'):
        newx,newy=up(x,y)
        return state[(newx,newy)]
    if(action=='D'):
        newx,newy=down(x,y)
        return state[(newx,newy)]
    

def max_reward(s):

    x,y = coordinate[s]
    r=[]
    if(is_safe(left(x,y))):
        r.append(['L',q[(s,'L')]])
    if(is_safe(right(x,y))):
        r.append(['R',q[(s,'R')]])
    if(is_safe(up(x,y))):
        r.append(['U',q[(s,'U')]])
    if(is_safe(down(x,y))):
        r.append(['D',q[(s,'D')]])
    
    random.shuffle(r)
    return max(r,key=lambda x: x[1])


q={}
for i in range(len(state)):
    q[(i,'L')]=0
    q[(i,'R')]=0
    q[(i,'U')]=0
    q[(i,'D')]=0

current_state = 22
gamma = 0.8
total_reward=0
while True:

    # print(x,y)
    action,reward = max_reward(current_state)
    total_reward += reward
    # updating the q function for current state
    q[(current_state,action)]=gamma*reward

    new_state = next_state(current_state,action)
    print(coordinate[current_state],coordinate[new_state])
    break