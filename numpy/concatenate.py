# Concatenate
import numpy as np
a=np.array([3,4,2,6])
b=np.array([8,6,5,10])
print(np.concatenate((a,b)))

# append 1D
print(np.append(a,100)) # สมาชิกมาต่อท้าย

# append 2D
c=np.array([[1,2],[3,4]])
print(np.append(c,[[10],[20]],axis=1))