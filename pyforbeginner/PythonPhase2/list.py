# เขียนแบบ primitive
# a=1
# a1=2
# a2=3
# a3=4
# a4=5

# non primitive : list
# List ข้อมูลสามารถแก้ไขได้ 
# number=[] # list ว่าง 
# number=[1,2,3,4,5,6] # list มีสมาชิก 1-6
# number=["นาย A","นาย B","นาย C"] # list name มีสมาชิก
# all=[10,"นายไข่",True,3.14,-10]

# #construtor
# name = list(["นาย A","นาย B","นาย C"])

# print(name)

# # เข้าถึงข้อมูลของ List
# print(number[2])
# print(all[2:])


# # การแก้ไขข้อมูล
# # ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"
# number=[1,2,3,4,5,6]
# print("ก่อนแก้ไข => ",number)
# number[2]=9
# number[-1]="นายไข่"
# print("หลังการแก้ไข => ",number)



# number=[1,2,3,4,5,6,4,8,4,6,2,1,3,4,5,6,7,1]
# fruit = ["mango","Yellow","banana","apple"]

# for i in range(len(fruit)):
#     print(fruit[i])

# for item in fruit:
#     print(item)


# # append() นำสมาชิกใหม่ มาต่อท้าย
# fruit.append("tomato")
# print(fruit)

# # insert (index,สมาชิกใหม่) เป็นการแทรก
# fruit.insert(1,"papaya")
# print(fruit)

# remove
# fruit.remove("Yellow")
# print(fruit)

# # pop ลบข้อมูลจากขวาสุดออก
# fruit.pop()
# fruit.pop()
# print(fruit)

# del เคลียร์หน่วยความจำ
# del fruit
# print(fruit)

# clear ลบสมาชิกออกเป็นค่าว่าง
# fruit.clear()
# print(fruit)

# การคักลอกข้อมูล
# x=[]
# print(x)
# x=fruit.copy()
# print(x)

# การรวมข้อมูล
# allgroup=number+fruit
# print(allgroup)
# number.extend(fruit)
# print(number)

# count
# x=number.count(5)
# print(x)


# Assignment1 เรียงลำดับข้อมูลตัวเลข
# number=[]
# while True:
#     x=int(input("Enter number: "))
#     if x<0:
#         break
#     number.append(x)
# print(number)
# number.sort() # น้อยไปมาก
# print(number)
# number.reverse() # มากไปน้อย
# print(number)


# Assignment2 min max
# number=[]
# while True:
#     x=int(input("Enter number: "))
#     if x<0:
#         break
#     number.append(x)
# print(number)
# print(min(number))
# print(max(number))
# print(sum(number))


# Assignment3 odd even
# number=[]
# even=[]
# odd=[]
# while True:
#     x=int(input("Enter number: "))
#     if x<0:
#         break
#     if x%2 ==0:
#         even.append(x)
#     else:
#         odd.append(x)
#     number.append(x)
# print(number)
# print(even)
# print(odd)


# Assignment4 เรียงลำดับชื่อ
# student=["สมพร","แก้ว","จอมขวัญ","อัมพร","ก้อง","กล้า"]
# print(student)
# student.sort()
# print(student)
# student.reverse()
# print(student)


# Assignment5 เรียงลำดับสมาชิกหลังสุดไปหน้าสุด
# fruit = ["mango","Yellow","banana","apple"]
# print(fruit)
# fruit=fruit[::-1]
# print(fruit)


# Assignment6 หาค่าเลขยกกำลัง
# number=[1,2,3,4,5,6,4,8,4,6,2,1,3,4,5,6,7,1]
# print(number)

# normal
# for i in range(len(number)):
#     number[i]=number[i]**2
# print(number)

#ลดรูป
# number=[i*i for i in number]
# print(number)


# Assignment7 จับคู้คำทักทาย
# greeting= ["Hi","Hello","Yeah","GN"]
# people=["Jan","Jam","Jab"]
# result=[]
# result=[x+y for x in greeting for y in people]
# print(result)


# Assignment8 จับคู่สินค้าและราคา
# fruit = ["mango","Yellow","banana","apple"]
# price = ["15","20","35","40"]

# for x,y in zip(fruit,price[::-1]):
#     print(x,y)


# Assignment9 การค้นหาและนับจำนวนตัวอักษร
message=["aa","aab","aaab","aaaab"]
result=[]
for item in message:
    result.append(item.count("a"))
print(result)