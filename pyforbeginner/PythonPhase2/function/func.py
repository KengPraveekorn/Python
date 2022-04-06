# การสร้าง function / เรียก function

# def ชื่อฟังชั่น () :
#       statement คือกลุ่มคำสั่ง

# def sayHi():
#     print("Hello Function")

# def saythai():
#     print("สวัสดี")

# def sayEngland():
#     print("Hello / Hi")

# def add():
#     x=3+1
#     print(x)
# # Main program
# sayEngland()

# for i in range(4):
#     add()


# function return ค่า

"""
1.ไม่มีการรับค่าและส่งค่า
def name():

2.มีการรับค่าเข้าไปทำงาน
def name(a,b):

3.รับค่าเข้าไปทำงาน และส่งออกมา
def name(a,b):
    return a+b

4.ไม่มีการรับค่าเข้ามา แต่ส่งค่าออกไป
"""

# def add(a,b):
#     return a+b

# def showNumber():
#     return 500

# x=add(1,2)
# print(x)
# print(showNumber())



def randomNumber(x):
    if x == "100":
        print("ถูกหวย")
        return 1000
    else:
        print("ไม่ถูกหวย")
        return 0

money = randomNumber("100") # ตัวแปร money เก็บค่า return  
x = 300
result = money-x
print("เงินรางวัล = ",money)
print("เงินคงเหลือ = ",result)