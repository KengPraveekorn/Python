# Math Operator 1D
import numpy as np
a=np.arange(1,5)
print(a+2)
print(a+10)
print(a-5)
print(a*2)
print(a**2)
print(a%2)
print(a/2)

print(a.shape)

b=np.arange(1,5)
print(a+b) # จะบวกกันได้ต้องมีขนาด array เท่ากัน

print(b.shape)

# Math Operator 2D
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])
print(x.shape)
print(y.shape)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x%y)

# Broad casting ทำงานที่ array ที่มีขนาดเล็กกว่าและถูกทำซ้ำ
   
print(x+[2])

z=np.array([1,2,3])
print(z.shape)
print(x+z)
