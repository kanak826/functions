#function deffination...
def cal_sum(a,b):   #parameters
    sum =a +b
    print(sum)
    return sum
cal_sum(5,6)#function call; give arguments...
#............................................................
def cal_diff(a,b):
    diff = a-b
    print(diff)
    return diff
cal_diff(5,4)
#..............................................................

def print_hello():
    print("hello")#hello
ob=print_hello() #none
print(ob)   
#................................................................

def cal_mul(a,b=8):
    mul=a*b
    return mul
ob=cal_mul(5)
print(ob)  
#..................................................................

movies=["Helen keller","Aryabhata","chetak"]
Reallife_heroes=["kailash shatyarthi","Malala yousoufjaii"]

def print_len(list):
    print(len(list))
def print_list(list):
    for item in list:
        print(item,end=" ")

print_len(movies)
print_len(Reallife_heroes)

#...................................................................

n=5
fact=1
for i in range(1,n+1): # convert this in function
 fact*=i
print(fact)  

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact) 
cal_fact(4)       
#..................................................................

def convertor(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")
convertor(100)    
# ...................................................................

# RECURSION......function calls itself repeatedly..

# ..............................

def show(n):
    if(n==78):
        return
    print(n)
    show(n+1)
    print("loop end")

show(9)    
#.........................................................................

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(4))    

#.........................................................................
def calc_sum(n):
    if n==0:
        return 0
    return calc_sum(n-1)+n    
    # 
sum = calc_sum(10)
print(sum)         
#........................................................................
# 
# oops.......................................................................
# 
class Car:
    color="blue"   #class forming
    brand="Thar"

car1=Car()
print(car1.color)  #object forming
print(car1.brand)
# ............................................................................

# class & instances Attributes
# self.name(instance or object attribute)
#attributes means properties of an object
 #...........................................................................

class Student:
    college_name ="TIT college"  #class attributes #common for all objects

    def __init__(self):  #default constructor
        print("hello")

    def __init__(self,name,age):  #it has multiple parameter  so it is called paramaterized constructor    
        self.name=name #object attribute
        self.age=age
        print("adding new student")
    def wlcm(self):#method forming 
        print("wlcm students",self.name)

s2=Student("kanak",18)#these paranthesis use for calling constructor
s2.wlcm()
print(s2.wlcm)
print(s2.name ,  s2.age)
print(s2.college_name)
#.............................................................................

# METHODS......................................................................

# methods means how the function is work.....like how it move ,start stop,run,and etc.
# methods are function belongs to objects

# static method...............has not (self)parameter
# it perform function for class attributes not for objects
# for forming normal fn. made by user it remove error by written
# @staticmethod before forming your function...and#
 #work as methodand 
#it is known as decorator.

#..............................................................................

 