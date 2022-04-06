# การเข้าถึงข้อมูลใน Series (แบบช่วงข้อมูล)
import pandas as pd
ps=pd.Series([10,20,30,40,50,60,70,80,90,100])
print(ps)
print(ps[3])

print(ps[1:]) # index1 จนถึงสุดท้าย
print(ps[4:]) # index4 จนถึงสุดท้าย
print(ps[:5]) # index0 จนถึงสุดท้าย index5
print(ps[:3]) # index0 จนถึงสุดท้าย index5
print(ps[1:8]) # index1 จนถึง index7
