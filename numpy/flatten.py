#Flatten
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a.flatten()) # Change 2D to 1D แต่ไม่เปลี่ยนถาวร

b=a.flatten()

c=a.ravel() # เปลี่ยนถาวร
print(c)
c[0]=5
print(c)