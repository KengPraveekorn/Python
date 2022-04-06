# สร้าง Series จาก numpy
import pandas as pd
import numpy as np
ndata=np.array([10,20,30,"Praveekorn","iphone",True])
print(ndata)

ps=pd.Series(ndata)
print(ps)