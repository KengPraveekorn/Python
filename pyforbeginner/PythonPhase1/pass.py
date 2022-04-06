# pass การให้โปรแกรมรันผ่านไปไม่สนใจมีไว้สำหรับวางโครงสร้างโค้ด

age = int(input("ป้อนอายุของคุณ: "))

if age<=15:
    if age==15:
        pass
    elif age==14:
        pass
    elif age==13:
        print("ม.1")
    else:
        print("ประถม")
else:
    print("มัธยม")


print("จบโปรแกรม")