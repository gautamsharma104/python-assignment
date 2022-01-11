#question 1

print("question1")

#average of three numbers

a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

add = a + b +c 
average = add/3
print("addistion is", add)
print("average of three numbers is" , average)

print()

#question2

print("question2" )

Gross_income = int(input("enter the Gross income :"))
depondent = int(input("no  of depondent is :"))
#standerd deduction = $10,000
#depondent deduction = $3,000
taxable_inco = Gross_income - 10000 - (depondent * 3000)
#tax rate = 20%
tax = taxable_inco * (.20)
print("taxable income is :", taxable_inco,'$' )
print("tax is:" ,tax,'$')

print()

#question  3

print("question3")

# making of list

NAME = "RADHEY"
SID = 21104580
GENDER = "M"
COURSE = "EE"
CGPA = 7.8
list = [NAME,SID,GENDER,COURSE,CGPA ]
print(list)

print()

#question 4

print("question4")

m1 = int(input("enter the marks of first student :"))
m2 = int(input("enter the marks of second student :"))
m3 = int(input("enter the marks of third student :"))
m4 = int(input("enter the marks of fourth student :"))
m5 = int(input("enter the marks of fifth student :"))

list = [m1,m2,m3,m4,m5]
list.sort()
print(list)


print()

#question 5(a)
print("question 5(a)")

list = ['RED','GREEN','white','BLACK','PINK','YELLOW']

list.remove('BLACK')
print(list)
print()

#5(b)

print("5(b)")

list = ['RED','GREEN','white','BLACK','PINK','YELLOW']

list.remove('BLACK')
list.remove('PINK')
list.append('Purple')
print(list)

