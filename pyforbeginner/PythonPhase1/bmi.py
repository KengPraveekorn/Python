# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (Kg) / ส่วนสูง*ส่วนสูง (m)
# input / convert to integer
weight = int(input("ป้อนน้ำหนักของคุณ (Kg): "))
high = int(input("ป้อนส่วนสูงของคุณ (cm): "))/100
print("BMI = ",weight/(high**2))
 