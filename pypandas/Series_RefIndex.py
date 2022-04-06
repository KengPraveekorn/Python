# การเข้าถึงข้อมูลใน Series (อ้างอิง Index)
import pandas as pd
data = [10,20,30,40]
print(data)

a=pd.Series(data)
print(a)
print(a[2]) # Series a index2

color={"green":"เขียว","red":"แดง","yellow":"เหลือง"}
b=pd.Series(color)
print(b)
print(b["red"])
print(b["green"])
print(b["yellow"])
