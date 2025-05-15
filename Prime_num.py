import math
def is_Prime(num):
    if num<=1 : 
        return False
    for i in range (2, int (math.sqrt(num))+1):
        if num % i == 0:
            return False
        return True
num=int(input("enter num "))
if is_Prime(num):
        print(f"{num}is a prime number")
else:
        print(f"{num}is not prime number")    