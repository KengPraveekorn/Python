# Slice 1D array a[start:end+1] 
import numpy as np
a=np.arange(1,11)
print(a[:])
print(a[2:])
print(a[:5])
print(a[2:9:2])
print(a[::2])

b=np.array([20,10,30,50,40])
print(b[:3])
print(b[1:3])


# Slice 2D array x[start:,end:] row and column
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x[:,:])
print(x[1:,:])
print(x[1:,1:])
print(x[1:2,1:2])
print(x[:2,2:])
print(x[1:2,:])
print(x[::,::2])
print(x[::,1:2])
