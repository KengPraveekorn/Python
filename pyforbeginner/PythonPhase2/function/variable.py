# Global variable / Local variable

def displayNumber():
    x=50
    a=100
    print("Hello = ",a,"ใน")

# main program
a=200
displayNumber()
print("นอก = ",a)

# นาย x ดารา => x ทั่วประเทศรู้จัก (Global)
# นาย x หมู่บ้านแสนสุข => x ในหมู่บ้าน (Local)


# การส่งค่าเข้ามาใน function
def myData(name,lname,c):
    print("ชื่อ = ",name,"นามสกุล = ",lname,"อายุ = ",c)

fname="Keng"
lname="Praveekorn"
age=23
myData(fname,lname,age)