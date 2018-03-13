import random
import time

# board dimensions
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

# defining the state coordinate mapping
state={}
coordinate={}
label=0
for i in range(m):
    for j in range(n):
        state[(i,j)]=label
        coordinate[label]=(i,j)
        label+=1

# defining the q values for each state action pair
q={}
for i in range(len(state)):
    q[i]=0

# making all the states un-visited
visited = {}
for i in range(len(state)):
    visited[i]=0

# defining funtion
def get_state(x,y):
    return state[(x,y)]

def get_coordinate(state):
    return coordinate[state]

def is_safe(x,y):
    # print(x,y)
    if(x>=0 and y>=0 and x<n and y<m and board[x][y] != '#'):
        if(visited[get_state(x,y)] != 1):
            return True
    return False

def left(s):
    x,y = get_coordinate(s)
    return get_state(x,y-1)

def right(s):
    x,y = get_coordinate(s)
    return get_state(x,y+1)

def up(s):
    x,y = get_coordinate(s)
    return get_state(x-1,y)

def down(s):
    x,y = get_coordinate(s)
    return get_state(x+1,y)

def next_state(s,action):
    if(action=='L'):
        return left(s)
    if(action=='R'):
        return right(s)
    if(action=='U'):
        return up(s)
    if(action=='D'):
        return down(s)
    
def max_reward(s):

    r=[]
    x,y=get_coordinate(s)
    if(is_safe(x,y-1) and not visited[left(s)]):
        r.append(['L',q[left(s)],left(s)])

    if(is_safe(x,y+1) and not visited[right(s)]):
        r.append(['R',q[right(s)],right(s)])
    
    if(is_safe(x-1,y) and not visited[up(s)]):
        r.append(['U',q[up(s)],up(s)])

    if(is_safe(x+1,y) and not visited[down(s)]):
        r.append(['D',q[down(s)],down(s)])
    if(r):
        random.shuffle(r)
        return max(r,key=lambda x: x[1])
    
    # empty move
    return ('E',0,0)


current_state = 25
final_state = 16
# second last state
q[16]=10
visited[current_state]=1
print("Current coordiante : {}".format(coordinate[current_state]))
gamma = 0.8
total_reward=0
r=0
episode = 0
epoch=0
while True:

    epoch+=1
    action,q_reward,next_state = max_reward(current_state)
    if(action != 'E'):
        q_new= (r+((gamma**epoch)*q_reward))
        total_reward += q_new
        # updating the q function for current state
        q[current_state] = q_new

        # bot moves to next state
        current_state = next_state
        visited[next_state]=1
        x,y=coordinate[next_state]


        # print('intermediate cooridiante : {}'.format((x,y)))
        if(board[x][y]=='$'):
            # one episode complete
            episode+=1
            print("Final coordinate : {}".format((x,y)))
            print("Total reward after episode {} : {}".format(episode,total_reward))
            print(q)
            # restarting the game
            # bringing the bot at the start
            # intitializing the rewards as 0
            total_reward=0
            current_state=25
            epoch=0
            for i in range(len(state)):
                visited[i]=0
            visited[current_state]=1

            print("Restarting the game ....")
            time.sleep(2)
            print("Current coordiante : {}".format(coordinate[current_state]))


    else:
        # restarting the game
        # bring the bot at the start state
        # intitializing the rewards as 0
        total_reward=0
        current_state=25
        epoch=0
        for i in range(len(state)):
            visited[i]=0
        visited[current_state]=1


        print('No moves left, restarting the game ...')
        time.sleep(2)
        print("Current coordiante : {}".format(coordinate[current_state]))
    

    # <--------------------- end -------------------->