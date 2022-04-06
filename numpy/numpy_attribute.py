import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b.ndim)
print(b.dtype)

# Shape บ่งบอกลักษณะของ array 
print(a.shape) # 1D บอกจำนวนสมาชิกในแถว
print(b.shape) # 2D บอกแถว บอกคอลัม

# Size บ่งบอกสมาชิกใน array
print(a.size)
print(b.size)

# itemsize บ่งบอกถึงขนาดว่ามีกี่ byte
print(a.itemsize)
print(b.itemsize) # int32 32bit/8bit = 4byte

c=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="complex")
print(c.itemsize) # complex128 128 bit/8 bit = 16 byte