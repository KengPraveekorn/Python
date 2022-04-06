# Index Operator  นำข้อมูลไปยัดใส่ใน array แล้วไปใส่ใน array หลักอีกทีนึง
import numpy as np
x=np.arange(1,10)
index=np.array([1,5,7])
print(x[index]) # x สมาชิก index ที่ 1,5,7

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[[0,2]])
print(b[[0,2],[2,0]])
print(b[[0,2],[2]])
print(b[[0,2],[1]])

print(x[2]) 

m=x[[1,4,1,4,1,4,1,4]]
print(m)

x=np.array([[1,-2,3],[4,-5,-9]])
print(x[x<0])
print(x[x>2])
print(x[x<0]*-1)
print(x[x<0]*2)
print(x[x<0]**2)