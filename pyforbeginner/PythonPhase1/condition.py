#age = int(input("ป้อนอายุของคุณ: "))

# if age>=15:
#     print("คำนำหน้าเป็น นาย/นางสาว")
#     print("จบโปรแกรมด้านใน if")

# print("จบโปรแกรม")


# if age>=15 or age <=20:
#     print("วัยรุ่น")
# elif age>=20 or age<=29:
#     print("วัยทำงาน")
# else:
#     print("วันเด็ก")
# print("จบโปรแกรม")


# Ternary Operator
# print("วัยรุ่น") if age>=15 else print("วันเด็ก")


# if ซ้อน if
# if age<=15:
#     if age==15:
#         print("ม.3")
#     elif age==14:
#         print("ม.2")
#     elif age==13:
#         print("ม.1")
#     else:
#         print("ประถม")
# else:
#     print("มัธยม")


# print("จบโปรแกรม")


# เขียนโปรแกรมหาตัวเลข มาก / น้อย
# a=int(input("ป้อนตัวเลขที่ 1:"))
# b=int(input("ป้อนตัวเลขที่ 2:"))

# if a>b:
#     print(a," มากกว่า ",b)
# else:
#     print(b," มากกว่า ",a)


# หาเลขคู่ / คี่
# number = int(input("ป้อนตัวเลขของคุณ: "))
# # ถ้าหาร 2 ลงตัว => คู่
# if number %2 == 0:
#     print("เป็นเลขคู่")
# else:
#     print("เป็นเลขคี่")


# แลกแบงค์ธนาคาร
# number = int(input("เงินของคุณ: "))

# if number>=1000:
#     print("1000 bath = ",number//1000,"ใบ")
#     number%=1000

# if number>=500:
#     print("500 bath = ",number//500,"ใบ")
#     number%=500

# if number>=100:
#     print("100 bath = ",number//100,"ใบ")
#     number%=100

# if number>=50:
#     print("50 bath = ",number//50,"ใบ")
#     number%=50

# if number>=20:
#     print("20 bath = ",number//20,"ใบ")
#     number%=20


# แปลง ค.ศ. เป็น พ.ศ. +543
# แปลง พ.ศ. เป็น ค.ศ. -543
# number = int(input("ป้อนปี พ.ศ.: "))
# number=number-543
# print("เป็น ค.ศ. = ",number)


# BMI 
weight = int(input("ป้อนน้ำหนักของคุณ (Kg): "))
high = int(input("ป้อนส่วนสูงของคุณ (cm): "))/100
bmi = weight/(high**2)

if bmi>=0 and bmi<18.0:
    result="ผอม"
elif bmi>=18.5 and bmi<=22.9:
    result="สมส่วน"
elif bmi>=23.0 and bmi<=24.9:
    result="น้ำหนักเกิน"
elif bmi>=25.0 and bmi<=29.9:
    result="โรคอ้วนระดับ1"
elif bmi>30:
    result="โรคอ้วนระดับอันตราย"
else:
    result="ไม่ทราบค่าที่ชัดเจน"

print(result)
