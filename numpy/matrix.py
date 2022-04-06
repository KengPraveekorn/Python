# Zero Matrix สมาชิกเป็น 1 ทุกตัว
import numpy as np

a=np.zeros(5)
print(a)
print(np.zeros(5))
print(np.zeros((2,2)))

print(np.zeros((3,3))) # Matrix จตุรัส


# Ones Matrix สมาชิกเป็น 0 ทุกตัว
print(np.ones(10))
print(np.ones(10,dtype="int"))


# Matrix ค่าคงที่ full
print(np.full(5,10)) # ต้วเลขข้างหน้า => จำนวนสมาชิก / ตัวเลขข้างหลัง => ค่าคงที่
print(np.full((3,3),7)) # 3แถว 3คอลัม ค่าคงที่ = 7


# Identity Matrix สมาชิกเส้นทะแยงเป็น 1 ค่าอื่นเป็น 0 
print(np.identity(4)) # row and column ต้องเท่ากัน
print(np.eye(3,4)) # row and column ไม่จำเป็นต้องเท่ากันก็ได้
print(np.eye(5,k=1)) # ย้ายตน.ของเลข1 ด้วยค่าK ถ้าเป็น + จะย้ายขึ้น - ย้ายลง