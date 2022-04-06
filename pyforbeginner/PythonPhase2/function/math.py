# Factorial function
# def factorial(number):
#     if number==1:
#         return number
#     else:
#         return number*factorial(number-1)

# x=factorial(4)
# print(x)


# Fibonacci number
#0,1,1,2,3,5,8,...

# f0 = ? , f1 = ?
def fibonacci(number): 
    if number<=1 :
        # เลข 2 ลำดับแรก
        return number
    else:
        #เลขลำดับถัดไป
        return fibonacci(number-1) + fibonacci(number-2)

for i in range(10): #0,1,1,2,3
    print(fibonacci(i))