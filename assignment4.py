#question1
print('question1')

n= int(input(" enter the number of disks \n " ))
def hanoi(n,a,b,c):
    if n==1:
        print(n, 'disk move from', a ,'to', c)
    else:
        hanoi(n-1,a,c,b)
        print(n ,'disk move from', a ,'to', c)
        hanoi(n-1,b,a,c)
        

a = "sourse"
b= "helper"
c= "destination"
hanoi(n,a,b,c)

print()
#question2
print('question2')

n= int(input('enter the number of rows:\n '))
list1=[]
for i in range(n):
    list2=[]                 # inner list of list1
    for j in range (i+1):
        if j==0 or j ==i:
            list2.append(1)
        else:
            list2.append(list1[i-1][j-1]+ list1[i-1][j])
    list1.append(list2)
print(list1)       


for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(list1[i][j],end=" ")
    print()    


print()
#question3
print('question3')
num1 = int(input('first number is: \n '))
num2 = int(input('second number is: \n '))  #num2 =! 0

A= num1/num2
B= num1%num2
print(A)
print(B)

print()
#a
print('a')
print(callable(A))
print(callable(B))

print()
#b
print('b')
if num1==0 :
    print("all values are not non zero")

else:
    print("values are not equal to zero")

  
print()
#c
print('c')

y = (4,5,6)
list1 = list(y)
list1.append(A)
list1.append(B)
print(list1)
list2=[]
for i in list1:
    if i>4:
        list2.append(i)
print(list2)

print()
#d
print('d')
set1= set(list2)
print(set1)

print()
#e
print('e')
tp1= tuple(set1)
print(tp1)

print()
#f
print('f')
print(max(set1))

print()
#question(4)
print("question(4)")
print()
class student:


    def __init__(self,Name,Rollnumber):
        self.name  = Name
        self.rollnumber = Rollnumber
        print("The name of student is", self.name, "and rollnumber is",self.rollnumber )

    def __del__(self):
        print("object rohan is deleted")

rohan = student("ROHAN",55)
del(rohan)

#question5
print()
print("question5")


class Employees :

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def details(self):
        print("Employee  name is", self.name,"and salary is ",self.salary, "Rupess")
        


    def __del__(self):
        print("Employee",self.name,"  is deleted")

Employee1 = Employees('Mehak',40000)
Employee2 = Employees('Ashok',50000)
Employee3 = Employees('Viren',60000)

Employee1.details()
Employee2.details()
Employee3.details()


print()
#a
print('a')
Employee1.salary = 70000
Employee1.details()
print()
#b
print('b')
del(Employee3)
