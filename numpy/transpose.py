# transpose เปลี่ยนจากแนวตั้งเป็นนอน นอนเป็นตั้ง
import numpy as np 
a=np.array([[1,2,3],[4,5,6]])
print(a.transpose())

b=a.transpose()
print(a.shape)
print(b.shape)