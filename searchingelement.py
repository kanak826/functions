def search(list,n):
   i=0
   while i < len(list):
        if list[i]==n:
         
           return True
        i=i+1
        
   return False   
            
list=[1,4,5,7,34,98,8]
n=int(input("enter num:"))
if search(list,n):
    print("Found")
else:
    print("Not Found")    