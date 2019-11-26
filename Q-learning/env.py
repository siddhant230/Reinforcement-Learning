import numpy as np
import cv2
from PIL import Image
import pickle
import warnings,time
warnings.filterwarnings('ignore')

size=10
alpha=0.1
epochs=5000
discount=0.95

color={"f":(255,200,255),
       "p":(0,255,0),
       "e":(0,0,255)}

class blob:
    def __init__(self):
        self.x=np.random.randint(low=0,high=size)
        self.y=np.random.randint(low=0,high=size)
    def __sub__(self, other):
        return (self.x-other.x,self.y-other.y)

    def move(self,x=False,y=False):
        if not x:
            self.x+=np.random.randint(-1,2)
        else:
            self.x+=x
        if not y:
            self.y+=np.random.randint(-1,2)
        else:
            self.y+=y

        if self.x<0:
            self.x=0
        elif self.x>size-1:
            self.x=size-1
        if self.y<0:
            self.y=0
        elif self.y>size-1:
            self.y=size-1

    def action(self,choice):
        if choice==0:
            self.move(x=1,y=1)
        elif choice==1:
            self.move(x=-1,y=-1)
        elif choice==2:
            self.move(x=-1,y=1)
        elif choice==3:
            self.move(x=+1,y=-1)
q_table={}
show=False
pivot=2
epsilon=0.9
decay=0.9998

with open("C:\\Users\\tusha\\Desktop\\q_table911_update.pickle","rb") as f:
    q_table=pickle.load(f)

enemy_penalty=300
food_reward=25

move_reward=1
episode_rewards=[]
for epoch in range(epochs):
    player=blob()
    enemy=blob()
    food=blob()
    episode_reward=0
    if epoch%pivot==0:
        print('average {} on epoch {}'.format(np.mean(episode_rewards[-pivot:]),epoch))
        show=True
    else:
        show=False

    for i in range(5):
        observation=(player-food,player-enemy)
        #if np.random.random()>epsilon:
        action=np.argmax(q_table[observation])

        #else:
        #   action=np.random.randint(0,4)

        player.action(action)
        #time.sleep(0.2)
        if player.x==enemy.x and player.y==enemy.y:
            reward=-enemy_penalty
        elif player.x==food.x and player.y==food.y:
            reward=food_reward
        else:
            reward=-move_reward

        new_observation=(player-food,player-enemy)
        max_future_q=np.max(q_table[new_observation])
        current_q=q_table[observation][action]

        if reward==-enemy_penalty:
            new_q=-enemy_penalty
        elif reward==food_reward:
            new_q=food_reward
        else:
            new_q=(1-alpha)*current_q + alpha*(reward+discount*max_future_q)

        q_table[observation][action]=new_q

        if show:
            env=np.zeros((size,size,3),dtype=np.uint8)
            env[food.x][food.y]=color['f']
            env[enemy.x][enemy.y]=color['e']
            env[player.x][player.y]=color['p']

            img=Image.fromarray(env,"RGB")
            img=np.array(img.resize((300,300)))
            cv2.imshow('SIMULATION',img)
            if reward==food_reward or reward==enemy_penalty:
                if cv2.waitKey(500)==ord('q') & 0xFF==ord('q'):
                    break
            else:
                if cv2.waitKey(4)==ord('q'):
                    break
        episode_reward+=reward
    episode_rewards.append(episode_reward)
    epsilon*=decay

with open("C:\\Users\\tusha\\Desktop\\q_table911_update.pickle","wb") as wf:
    pickle.dump(q_table,wf)
