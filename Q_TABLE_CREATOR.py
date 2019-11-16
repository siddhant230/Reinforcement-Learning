import pickle
import numpy as np

size=10
q_table={}
for x1 in range(-size+1,size):
    for x2 in range(-size+1,size):
        for y1 in range(-size+1,size):
            for y2 in range(-size+1,size):
                q_table[((x1,x2),(y1,y2))]=[np.random.uniform(-5,0) for i in range(4)]

with open("C:\\Users\\tusha\\Desktop\\q_table911.pickle","wb") as f:
    pickle.dump(q_table,f)
