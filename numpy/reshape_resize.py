#Reshape Resize
import numpy as np
a=np.arange(10)
print(a.reshape((2,5))) # เปลี่ยน 1D to 2D จะไม่มีการเปลี่ยนแปลงข้อมูลถาวร

b=a.reshape((2,5)) 
print(b)

print(a.resize((2,5))) # เปลี่ยนแปลงโครงสร้างข้อมูล array ให้ถาวรเลย
print(a)