# สร้าง Series แบบกำหนดหมายเลข Index
import pandas as pd
items=["มะม่วง","กล้วย","องุ่น"]
print(items)

idx = [50,20,30]
print(idx)

print(pd.Series(items,index=idx)) # เลข index ต้องมีจำนวนเท่ากัน