# สร้าง Series จาก List and Tuple
import pandas as pd
data_ls=[10,20,30,"Degang","Iphone",True]
print(data_ls)

# สร้าง Series จาก List
print(pd.Series(data_ls))
ps_ls=pd.Series(data_ls)
print(ps_ls)

# สร้าง Series จาก Tuple
data_tp=(10,20,30,"Degang","Iphone",True)
ps_tp=pd.Series(data_tp)
print(ps_tp)