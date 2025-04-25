#Calculation of simple interest ...

# step-1 = principle , rate ,time (take as parameter)
#step-2 = print each of them
# step-3 = apply formula
# step-4 = calling function 

#*********************************************************

def simple_interest():
    Principle = int(input("Enter Principle = "))
    Rate = int(input("Enter Rate = "))
    Time = int(input("Enter Time  = "))

    print((Principle*Rate*Time)/100)

simple_interest()
print("simple_interst is calculated ")
    
