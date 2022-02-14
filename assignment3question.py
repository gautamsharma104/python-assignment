# que1
#cherecter occurence
str1 = input("write a string here \n")
list1 = []
for ch in str1:
    if ch not in list1:
        list1.append(ch)
        print(ch, "occur",str1.count(ch),"times" )

print()

#question2
print("question2")
# find the next date

year =  int(input(" enter the year: \n"))
month =  int(input(" enter the month: \n"))
day =  int(input(" enter the day: \n"))

print(day,'/',month,'/',year)

if 1800<=year<=2025 and 1<=month<=12 and 1<=day<=31:
     if day ==31 and (month== 1 or month == 3 or month==5 or month == 7 or month ==8 or month== 10 ):
         print("next date is 1/",month +1,"/",year )

     elif day ==31 and month==12 :
         print("next date is 1/1/",year+1 )

     elif month ==2 and day== 29 and year%4 ==0 :
         print("next date is 1/3/",year)

     elif day ==28 and month == 2 and year%4 ==0 :
         print(" next date is 29/2/",year )

     elif day ==28 and month ==2  and year%4 != 0:
         print("next date is 1/3/",year)

     elif day == 30 and (month==4 or month==6 or month==9 or month==11):
         print("next date is 1/",month+1,"/",year)

     elif day ==30 and (month== 1 or month == 3 or month==5 or month == 7 or month ==8 or month== 10 or month ==12 ):
         print("next date is ", day+1,"/",month ,"/", year )

     elif day ==29  and month != 2 and 1<=month<=12 :
         print( "next date is", day+1,"/", month,"/", year)

     elif 1<=day <28  :
         print("next date is" , day+1,"/",month,"/", year)

     elif day==28 and month != 2 :
         print( "next date is", day+1,"/", month,"/", year)
else:
    print("input date is invailid")

print()

#question3
print("question3")
#list of tuples

n = int(input("enter the number of element: "))
list1 =[]
for i in range(n):
    list1.append(int(input("enter the elemant: ")))
print(list1)

list2 = []
for i in list1:
    v= (i,i*i)
    list2.append(v)
print(list2)

print()

#question4
print("question4")
#performence record

grade = int(input( "enter the number:\n")) 

#dict1 ={grade:["letter grade,performance]}

dict1 = {10:["A+ , outstanding"],9:["A , excellent"],8:["B+ , very good"],7:["B , Good"],6:["C+ , Average"],5:["C , Below Average"],4:["D , POOR"]}
if 4<=grade<=10:
    print(dict1[grade])
else :
  print("Error")

print()

#question7
print("question7")
#febonachi sequence
num = int(input("enter the number: "))
n1 = 0
n2= 1
sum=0
if num<=0:
    print("please enter a positive number")
else:
    for i in range(0,num):
        print(sum, end=" ")
        n1=n2
        n2=sum
        sum =n1+n2

print()

#question8
#sets
print("question8")
print("A")
set1 ={1,2,3,4,5}
set2 = {2,4,6,8}
set3 ={1,5,9,13,17}
a = set1 - set2
b = set2- set1

print(a.union(b))

print()
print('B')
a1= a-set3        #a= set1 - set2
c = set3-set1     #b = set2- set1
print(a1|c|b)

print()
print('C')
print(set1&set2)

print()
print('D')
new_set ={1,2,3,4,5,6,7,8,9,10}
print(new_set - set1)

print()
print('E')
print(new_set -(set1|set2|set3))
