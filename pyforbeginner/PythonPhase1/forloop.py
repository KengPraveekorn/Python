# โครงสร้างควบคุมแบบทำซ้ำ 
# for รู้จำนวนรอบชัดเจน

#for i in range(start,stop,step) # กำหนดรอบ

# for i in range(1,4): # range เริ่มต้นที่ 0
#     print("รอบที่ = ",i)
#     for j in range(1,6):
#         print("ตำแหน่งที่ = ",j)
    

# แม่สูตรคูณ
# start = int(input("ป้อนแม่สูตรคูณเริ่มต้น = "))
# stop = int(input("ป้อนแม่สูตรคูณสุดท้าย = "))

# for x in range(start,stop+1):
#     print("แม่ = ",x)
#     for y in range(1,13):
#         print(x,"x",y," = ",(x*y))


# ตัวเลขขั้นบรรได
# last=int(input("ป้อนตัวเลข = "))
# for row in range(1,last+1):
#     for column in range(1,row+1):
#         print(column,end='')
#     print(" ")


# วาด4เหลี่ยม
number = int(input("ป้อนตัวเลข = "))
for row in range(number):
    for column in range(number):
        print("x",end="")
    print(" ")