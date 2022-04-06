# # list , tuple
# lis=["red","yellow","blue"]
# tup=("red","yellow","blue")

# print(lis[0])
# print(tup[0])


#dictionart => key (การเข้าข้อมูล), value (ค่าของข้อมูล)
# list , tuple => index , value

# การสร้าง dict
# ชื่อตัวแปร = {key:value,key:value,key:value}
# colors={"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว"}
# print(colors["red"])

# pets=dict({"dog":"หมา","cat":"แมว","lion":"สิงโต",True:"true",999:"number"})
# print(pets["dog"])
# print(pets.get(999))
# print(pets[True])

# pets[999]="No" # แก้ไขข้อมูล
# print(pets)

# pets.update({"blue":"สีน้ำเงิน","orange":"สีส้ม","dog":"ชิสุ"}) # ถ้า key ไม่ซ้ำให้เพิ่มข้อมูล ถ้า key ซ้ำให้แก้ไขข้อมูล
# print(pets)

# for item in pets.values():
#     print(item)

# for item in pets.keys():
#     print(item)

# for k,v in pets.items():
#     print("key = ",k,"value = ",v)

# pets.pop("dog")
# pets.popitem() #เอาสมาชิกตัวนอกสุดออกไป
# print(pets)

# pets.clear()
# print(pets)

# del pets
# print(pets)

# x=pets.copy()
# print(x)


#dictionart => key (การเข้าข้อมูล), value (ค่าของข้อมูล)
market={
    "ร้านป้าพร":{
        "name":"ป้าพร",
        "menu":["กะเพราไก่","ก๋วยเตี๋ยว"],
        "zone":"ตะวันออก"
    },
    "ร้านลุงป้อม":{
        "name":"ลุงป้อม",
        "menu":["มะม่วง","ทุเรียน"],
        "zone":"ทางเข้าตลาด"
    },
    "ร้านน้ำใจ":{
        "name":"น้ำใจ",
        "menu":["นมปั่น","ชาเย็น"],
        "zone":"ข้างเซเว่น"
    }
}

# print(market["ร้านป้าพร"]["menu"])

if "ก๋วยเตี๋ยว" in market["ร้านป้าพร"]["menu"]:
    print("Yes")
else:
    print("No")