# ลบสมาชิกใน Array 1D
import numpy as np
a=np.arange(1,10)
print(np.delete(a,2)) # delete index(2) 
print(np.delete(a,2)) # delete index(2) 


# ลบสมาชิกใน Array 1D
b=np.arange(1,13).reshape(4,3)
print(b)
print(np.delete(b,2,axis=0)) # delete indexแถวที่2
print(np.delete(b,2,axis=1)) # delete indexคอลัมที่2

