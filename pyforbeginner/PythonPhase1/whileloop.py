# โครงสร้างควบคุมแบบทำซ้ำ 
# while รู้จำนวนรอบไม่ชัดเจน

# i=1 #ตัวนับจำนวนรอบ
# summation = 0 #เก็บผลการบวกเลขตามจำนวนรอบ
# average = 0 #ผลรวม / จำวนรอบ

# count=int(input("ระบุจำนวนรอบ: "))

# while i<=count:
#     summation += i #เก็บผลรวมของ i แต่ละรอบ 1+ 2+3
#     print("รอบที่ = ", i ," ค่า sum = ",summation)
#     i+=1

# average=summation/count
# print("ผลรวมการบวกเลข = ",summation)
# print("ค่าเฉลี่ย = ",average)


# Loop ซ้อน Loop
i=1
while i<=3:
    j=1
    while j<=5:
        print("รอบที่ = ",i," ตำแหน่งที่ = ",j)
        j+=1
    i+=1
    