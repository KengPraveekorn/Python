# List Parameter

def displayFruit(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ ",i+1," = ", item[i])
        
def displayvet(item):
    for i in range(len(item)):
        print("ผักชนิดที่ ",i+1," = ", item[i])

fruit = ["mango","orange","banana"]
vet = ['kana','chaome','pukkad']

displayFruit(fruit)
displayvet(fruit)