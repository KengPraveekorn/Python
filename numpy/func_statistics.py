# Function Statistics 1D
import numpy as np
a=np.array([10,5,4,6,99,100,50,30])
print(a.sum()) # ผลบวก
print(a.prod()) # ผลคูณ
print(a.mean()) # ค่าเฉลี่ย
print(a.max()) # ค่าสูงสุด
print(a.min()) # ค่าต่ำสุด
print(a.argmax()) # ค่าตน.สูงสุด
print(a.argmin()) # ค่าตน.สูงสุด

# Function Statistics 2D
b=np.array([[10,20,30],[40,50,90],[80,100,5]])
print(np.min(b,axis=1)) # หาเลขต่ำสุดแนวนอน axis = 1(แกนนอน)
print(np.min(b,axis=0)) # หาเลขต่ำสุดแนวตั้ง axis = 0(แกนตั้ง)
print(np.max(b,axis=1)) # หาเลขมากสุดแนวตั้ง axis = 0(แกนตั้ง)
print(np.max(b,axis=0)) # หาเลขมากสุดแนวตั้ง axis = 0(แกนตั้ง)