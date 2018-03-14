import random
import time

class Game :

    def __init__(self,board):
        self.board = board

    def next_state(self,s,action):
        if(action=='L'):
            return self.board.left(s)
        if(action=='R'):
            return self.board.right(s)
        if(action=='U'):
            return self.board.up(s)
        if(action=='D'):
            return self.board.down(s)

    def max_reward(self,s):

        r=[]
        x,y=self.board.get_coordinate(s)
        if(self.board.is_safe(x,y-1) and not self.board.visited[self.board.left(s)]):
            r.append(['L',self.board.q[self.board.left(s)],self.board.left(s)])

        if(self.board.is_safe(x,y+1) and not self.board.visited[self.board.right(s)]):
            r.append(['R',self.board.q[self.board.right(s)],self.board.right(s)])
        
        if(self.board.is_safe(x-1,y) and not self.board.visited[self.board.up(s)]):
            r.append(['U',self.board.q[self.board.up(s)],self.board.up(s)])

        if(self.board.is_safe(x+1,y) and not self.board.visited[self.board.down(s)]):
            r.append(['D',self.board.q[self.board.down(s)],self.board.down(s)])
        if(r):
            random.shuffle(r)
            return max(r,key=lambda x: x[1])
        
        # no moves left,return empty move
        return ('E',0,0)

    def play(self,gamma,r):
        
        total_reward=0
        episode = 0
        epoch=0
        current_state = self.board.start_state
        final_state = self.board.final_state
        print("Start coordiante : {}".format(self.board.coordinate[current_state]))
        
        while True:
            epoch+=1
            action,q_reward,next_state = self.max_reward(current_state)
            self.board.visited[current_state]=1

            if(action != 'E'):

                q_new= (r+((gamma**epoch)*q_reward))
                total_reward += q_new
                self.board.q[current_state] = q_new
                current_state = next_state
                self.board.visited[next_state]=1
                x,y=self.board.get_coordinate(next_state)

                if(self.board.board[x][y]=='$'):
                    # one episode complete
                    episode+=1
                    print("Final coordinate : {}".format((x,y)))
                    print("Total reward after episode {} : {}".format(episode,total_reward))

                    # restarting the game
                    # bringing the bot at the start
                    # intitializing the rewards as 0
                    total_reward=0
                    current_state=25
                    epoch=0
                    for i in range(len(self.board.state)):
                        self.board.visited[i]=0
                    self.board.visited[current_state]=1

                    print("\nRestarting the game ....")
                    time.sleep(2)
                    print("Start coordiante : {}".format(self.board.coordinate[current_state]))
            
            else:
                # restarting the game
                # bring the bot at the start state
                # intitializing the rewards as 0
                total_reward=0
                current_state=25
                epoch=0
                for i in range(len(self.board.state)):
                    self.board.visited[i]=0
                self.board.visited[current_state]=1

                print('\nNo moves left, restarting the game ...')
                time.sleep(2)
                print("Start coordiante : {}".format(self.board.coordinate[current_state]))


