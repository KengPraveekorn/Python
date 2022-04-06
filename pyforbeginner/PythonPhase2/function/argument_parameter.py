# Arguments / Parameter

def myData(name,lname,c):
    print("ชื่อ = ",name,"นามสกุล = ",lname,"อายุ = ",c)

fname="Keng"
lname="Praveekorn"
age=23
myData(fname,lname,age)

# Arguments => ค่าที่ส่งเข้าไปใน function => fname,lname,age (ตอนที่เรียกใช้ function)
# Parameter => ค่าตัวแปรที่รับข้อมูลที่ส่งมาทำงาน (ค่ามาจาก arguments)
# อาส่ง - พารับ 


# Assignment คู่ / คี่
def searchNumber(number):
    if number%2 == 0:
        print("Even")
    else:
        print("Odd")

a,b,c,d = 10,23,40,50

searchNumber(a)