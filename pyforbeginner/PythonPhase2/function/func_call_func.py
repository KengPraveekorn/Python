# function call function

def equal(x,y,z):
    return compareMax(compareMax(x,y),z)

def compareMax(x,y):
    if x>y:
        return x
    else:
        return y

max = equal(3,6,-5)
print("ค่ามากที่สุด = ",max)


def displayFood():
    print("หูฉลาม")

def displayCity():
    print("CNX")
    displayFood()

displayCity()