# แปลง Temp
from unittest import result


temp = input("Enter temp: ")

degree = int(temp[:-1]) 
unit = temp[-1].upper() #C / upperคือแปลงให้เป็นตัวพิมใหญ่ lower คือแปลงเป็นพิมเล็ก


if unit=="C":
    #แปลงเป็น F
    result = (9*degree)/5 +32
    unit_result = "F"
if unit=="F":
    #แปลงเป็น C
    result = (degree-32)*5 /9
    unit_result = "C"

print("แปลงตัวเลข = ",temp," เป็น ",unit_result," = ",result)
