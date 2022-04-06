# เกมทายเลขลูกเต๋า
# 1,2,3,4,5,6

import random
# สุ่มตัวเลขลูกเต๋า
myramdom = random.randrange(1,7) # 1 - 6
k=1
correct = False
print("3 Ask")
while True:
    number=int(input("ป้อนคำตอบของคุณ: "))
    correct=(number==myramdom) # true/false

    if not correct:
        if(number>myramdom):
            print("น้อยกว่า")
        if(number<myramdom):
            print("มากกว่า")

    if correct:
        print("Correctly")
        break
    if number<0 or k==3:
        break
    k+=1
    
if not correct:
    print("Worng!")
    print("เฉลย =",myramdom)