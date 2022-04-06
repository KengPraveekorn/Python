# # Tuple ข้อมูลที่ไม่สามารถแก้ไขได้ เช่น ค่าคงที่ ค่าพาย
# tup = (1,2,3,4,"develop","เดฟ",True,3.99) #Tuple
# print(tup)

# lis= list(tup) # แปลงข้อมูลจาก tuple ให้เป็น list เพื่อแก้ไขข้อมูล
# lis[0] ="Web"

# tup=tuple(lis)
# print(tup) 

# # tuple => string
# character = ('k','e','n','g')
# name= "".join(character)
# print(name)

# string to tuple
x="develop"
y=tuple(x)
print(y)