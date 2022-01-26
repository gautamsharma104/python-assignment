#question 1

print("question1")
print()
#a
print("1a")
print()

x = "paython is a case sencitive language"
print(len(x))

#b
print()
print("1b")
print()

stri = "paython is a case sencitive language"
list1 =stri.split()
print(list1)
list2 = list1[-1::-1]
print(list2)
output = ' '.join(list2)
print(output)


#c
print()
print("1c")
print()

stri= "paython is a case sencitive language"
list1 =stri.split()

print(list1)
stri2 = list1[2:5]
print(stri2)
output = ' '.join(stri2)
print(output) 

#d
print()
print("1d")
print()

stri= "paython is a case sencitive language"
output = stri.replace("a case sencitive" , "object oriented")
print(output)

#e
print()
print("1e")
print()

stri= "python is a case sencitive language"
print(stri.index('a'))

#f

print()
print("1f")
print()

stri= "paython is a case sencitive language"
list1 =stri.split()

print(list1)
output = ''.join(list1)
print(output)

#question2
print()
print("question2")
print()

name = "GAUTAM SHARMA"
SID = 21104056
dep_name = "ELECRICAL ENGINEERING"
CGPA = 8.8
print('hay',name,'here!')
print('my SID is',SID)
print('i am from ',dep_name,'and my CGPA is',CGPA)

print()
#question3
print()
#a
a = 56         #binary 111000
b = 10         #binary 001010
print(a&b)

print()
#b
print(a|b)

print()
#c
print(a^b)

print()
#d
print(a<<2)  #after a<<2 : binary 100000
print(b<<2)   #after b<<2 : binary 101000

print()
#e
print(a>>2)   #after a>>2 : binary 001110
print(b>>4)    #after b>>4 : binary 000000

print()
#question4
print()
print("question4")


n1 = input("enter the first number ")
n2 = input("enter the second number ")
n3 = input("enter the third number ")

if n1>n2 and n1>n3:
    print("greater number is", n1)
elif n2>n3 and n2>n1:
    print("greater number is",n2)
else:
    print("greater number is",n3)

#question5
print()    
print("question5")
print()

x = str(input("enter a string :"))
word = "name"
if word in x:
    print('yes ,name is in the string')
else:
    print('no')
    
#question6
print()
print("question6")
print()

s1 = int(input("enter the first side: "))
s2 = int(input("enter the second side: "))
s3 = int(input("enter the third side: "))

if s3+s2 >s1:
        print("yes given lengths form a triangle")
elif s1+s3 >s2:
     print("yes given lengths form a triangle")
elif s1+s3 >s2:
     print("yes given lengths form a triangle")
else:
    print("no triangle form")
