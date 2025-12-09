# #Check whether the input number is divisible by 5
# num=int(input("Give the input number:"))
# if num/5:
#     print("number is divisible by 5")
# else:
#     print("number is not divisible by 5")
# #Compare two numbers and print which is larger.
# a=int(input("enter first number:"))
# b=int(input("enter 2nd number:"))
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("both numbers are equal")
# #Take 3 numbers and print the greatest
# a1=int(input("enter first number:"))
# b1=int(input("enter 2nd number:"))
# c1=int(input("enter 3rd number:"))
# if a1>b1 and a1>c1:
#     print("a1 is greater than all")
# elif b1>a1 and b1>c1:
#     print("b1 is greater than all")
# else:
#     print("c1 is greater than all")
#Check if a character is vowel or consonant.
#t(input("Grade C:"))

# if ch.lower() in "aeiou":
#     print("character is vowel")
# else:
#     print("character is consonent")
# #Check if a number is between 1 and 100.
# a=int(input("enter a number"))
# if a<=100:
#     print("number is between 1 and 100")
# else:
#     print("number is greater than 100")
#Ask for username and password. Print login successful or failed
# username=input("enter the username:")
# password=input("enter the password:")
# if username=="admin" and password=="12345":
#     print("password is successful")
# else:
#     print("password is failed")
#Take marks and print grade (A, B, C, D, Fail)
# marks=int(input("Enter the marks here:"))
# if marks>=90:
#     print("Grade A")
# elif marks>=80 and marks<=89:
#     print("Grade B")
# elif marks>=70 and marks<=79:
#     print("Grade C")
# elif marks>=50 and marks<=69:
#     print("Grade D")
# else:
#     print("Grade F")
# marks = int(input("Enter your marks: "))

# if marks >= 80:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 50:
#     print("Grade: D")
# else:
#     print("Fail")
#Check if a year is leap year or not.
# year=int(input("Enter the year:"))
# if (year %4==0 and year % 100!=0) or (year%400==0):
#     print("year is leap")
# else:
#     print("year is not leap")
#Create a list of 5 numbers and print the largest number.
list=[12,30,879,345,38]
largest=max(list)
print("the largest number: ",largest)
#Add a new element to a list using append().
number=[3,4,5,1,2]
#number.append(8)
#number.sort(reverse=True)
#number.remove(4)
#print(number)
#Print the first and last elements of a list
print("print 1st element:",number[0])
print("print last element:",number[-1])
#Create a tuple of 5 names and print the third one.
#fruits=("mango","apple","grape","banana","alichi")
#print("name of third fruit is:",fruits[2])
#Convert a tuple into a list
# my_list=list(fruits)
# print(my_list)
# print(type(my_list))
# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Convert to list
my_list = list(my_tuple)

print(my_list)
print(type(my_list))


