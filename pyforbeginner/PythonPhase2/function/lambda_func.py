# Lambda function สร้างฟังก์ชั่นที่ไม่มีชื่อ

"""
lambda arguments : expression

"""

# x=lambda name:name
# sum=lambda x,y : x+y
# multiply=lambda a,b : a*b

# result = multiply(5,10)
# print(x("Praveekorn"))
# print(sum(5,10))
# print(result)


def myPower(x):
    # x = ตัวเลข
    # a = เลขชี้กำลัง
    return lambda a: 5**a

y=myPower(5)
result=y(3)
print(result) 