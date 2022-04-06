# Linspace เหมาะสำหรับไปพอตกราฟ เป็นการกำหนดข้อมูลตามช่วงของตัวเลขที่กำหนด พร้อมกับระบุจำนวนว่าต้องการกี่จำนวน
import numpy as np
print(np.linspace(1,10))
print(np.linspace(1,5,4))
print(np.linspace(1,5,endpoint=False)) # ไม่เอาข้อมูลตัวสุดท้าย