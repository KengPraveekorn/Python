"""
จัดกลุ่มข้อมูลพื้นฐาน
List = [] ,ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้, ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Tuple = (), ข้อมูลต่างชนิดกัน , แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Set = {}, ข้อมูลต่างชนิดกัน , แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันไม่ได้ , ลำดับไม่แน่นอน

"""

# normal
# fruit={"มะม่วง","มะขาม","มะยม"}

# lis=["fishto","fishtawien"]
# #constructor
# fish=set(lis)
# print(fish)

# # เพิ่มข้อมูลสมาชิก
# fruit.add("orange")
# fruit.add("tomato")
# fruit.add(999)
# #เพิ่มสมาชิกหลายตัว
# fruit.update(["papaya","apple","kiwi"])

# # #Loop
# # for item in fruit:
# #     print("ข้อมูล =>",item)
# print(fruit)

# # #แสดงจำนวนสมาชิกใน set
# # print(len(fruit))

# # ลบและเพิ่มข้อมูลที่เราแก้ไข
# fruit.discard("มะยม")
# fruit.add("ทุเรียน")
# #fruit.clear()
# #del fruit
# print(fruit)


# union
# fruitA ={"banana","mango","orange","apple"}
# fruitB ={"apple","kiwi","topato","banana"}

# allFruit = fruitA.union(fruitB)
# print(allFruit)

# #update
# fruitA.update(fruitB)
# print(fruitA)

# #copy
# fruitC = fruitA.copy()
# print(fruitC)

# #difference
# fruitC=fruitA.difference(fruitB)
# print(fruitC)

# #intersec
# fruitC=fruitA.intersection(fruitB)
# print(fruitC)

# #หาค่าต่างแล้วเก็บข้อมูลไว้ใน A 
# fruitA.difference_update(fruitB)
# print(fruitA)

# #หาค่าเหมือนแล้วเก็บข้อมูลไว้ใน A 
# fruitA.intersection_update(fruitB)
# print(fruitA)


# #superset
# fish={"whale","mackerel","squid","dolphin","catfish","dogfish"}

# #subser
# x={"whale","mackerel"} 
# print(x.issubset(fish))


#frozen set แก้ไขไม่ได้
fruit=frozenset(["banana","mango","orange","apple"])
for item in fruit:
    print(item)