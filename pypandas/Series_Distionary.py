# สร้าง Series จาก Dictionary {Keys:Value}
import pandas as pd
color={"green":"เขียว","red":"แดง","yellow":"เหลือง"}
print(color)

print(pd.Series(color))