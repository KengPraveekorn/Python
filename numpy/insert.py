# Insert 1D
import numpy as np
a=np.array([1,2,4,5,8])
print(np.append(a,40))
print(np.insert(a,1,100)) # (array,index,value)
print(np.insert(a,(1,3),100)) # (array,index,value)

# Insert 2D
b=np.array([[1,2],[3,4]])
print(np.insert(b,1,100,axis=0))
print(np.insert(b,1,50,axis=1))
print(np.insert(b,1,[10,20],axis=0))