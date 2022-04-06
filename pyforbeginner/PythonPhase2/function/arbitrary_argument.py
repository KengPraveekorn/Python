# *args => ค่าใน parameter มีได้หลายค่า

# def add(*number):
#     sum=0
#     for i in range(len(number)):
#         sum+=number[i]
#     print(sum)

# add(10,5)
# add(10,5,6)


#**kwargs => ชื่อ parameter มีได้หลายชื่อ

def displayData(**kwargs):
    print(kwargs)

displayData(fname = "Praveekorn",lname = "Chianglnog", city="CNX")
displayData(fname = "Praveekorn",lname = "Chianglnog", city="CNX",status = "Have fun")