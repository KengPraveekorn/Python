import numpy as np
a=np.arange(1,21)
print(np.split(a,4)) # ต้องแบ่งให้เท่าๆกันได้
print(np.split(a,5))

a=a.reshape(5,4)
print(a)
print(np.hsplit(a,4)) # แบ่งเป็นแนวตั้ง
print(np.vsplit(a,5)) # แบ่งเป็นแนวนอน
