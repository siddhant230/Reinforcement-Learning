import pickle
import numpy as np

size=10
q_table={}
##here x1,x2,x3,x4 represents your required feature space
##for example for moving in a grid only four movements are allowed=>UP DOWN LEFT RIGHT. So, x1,x2,x3,x4 to cover all valid combinations.
##another example can be flappy bird...required feature space is either UP or DOWN. So, x1,x2.
for x1 in range(-size+1,size):
    for x2 in range(-size+1,size):
        for y1 in range(-size+1,size):
            for y2 in range(-size+1,size):
                q_table[((x1,x2),(y1,y2))]=[np.random.uniform(-5,0) for i in range(4)]

with open("C:\\Users\\tusha\\Desktop\\q_table911.pickle","wb") as f:
    pickle.dump(q_table,f)
