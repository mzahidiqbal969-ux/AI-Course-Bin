#Write a Python program that asks the user for their name and city, and then prints a sentence like:
#“My name is Ali and I live in Lahore.”
name="Ali"
city="Lahore"
print("My name is", name ,"and I live in", city)
# Ask the user to enter any word.
# Print the following:
# First 2 letters
# Last 2 letters
# Middle letter (only one)
# word= input("enter my word:")
# print("first 2 letters:", word[0:2])
# print("last 2 letters:", word[-2:-1])

# sentence=input("i love my pakistan")
# count=len(sentence.replace(" ",""))
# print("print the sentence without gap:",count)
#Create variables a, b, and c with values 5, 10, and 15. Print their sum.
a=5
b=10
c=15
print(a+b+c)
#Store your name, age, and city in three variables and print them in one sentence.
name="zahid"
age=38
city="Mahra"
print("my name is",name,"and my age is",age,"and i live in",city)
#Assign two numbers to variables and swap their values
a=5
b=10
print("before swapping")
print("a:",a)
print("b:",b)
a,b=b,a
print("\n after swapping")
print("a:",a)
print("b:",b)
#Create a variable radius and calculate the area of a circle. (πr²)
rad=5
pi=3.1414
area=pi*rad*rad
print(area)
#Store the price and quantity of an item in variables and print the total bill.
shoesprice=200
quantity=10
bill=shoesprice*quantity
print(bill)
#Create two variables: length and width. Find the perimeter of a rectangle.
len1=10
wid=3
perimeter=2*(len1+wid)
print(perimeter)
#Store an integer, float, and string in three variables and print their types
number=10
height=5.6
name="hassan"
print(type(number))
print(type(height))
print(type(name))
#Take your friend's name in a variable and print a welcome message.
name="hassan"
print("welcome",name)
#Create variables math, physics, chemistry and print the total marks.
math=70
physics=90
chemistry=80
print("total marks:",math+physics+chemistry)
#Assign two variables x=20 and y=6. Print the result of x+y, x−y, x×y, x÷y
x=20
y=6
value1=x+y
print(value1)
value2=x-y
print(value2)
value3=x*y
print(value3)
value4=x/y
print(value4)
#Take input from the user and print its data type
name=input("print my name:")
print(type(name))
#Convert a string "100" into integer and add 50 to it
str="100"
str=int("100")
print(str+50)
#Convert integer 12 into float and print the result
num1=12
print(float(num1))
#Create a list of your three favorite fruits.
list=["mangoes","apples","alichi"]
print(list)
#Create a tuple containing your five exam marks
marks=(78,45,67,78,79)
print(marks)
#Create a dictionary with keys: name, age, class
student={"name" :"ali","age":35,"class":"10th"}
print(student)
#Create a set with unique numbers and show it removes duplicates
s = {1, 2, 2, 3, 3}
print(s)
#Convert a float (e.g., 12.56) to integer
height2=12.56
print(int(height2))
#Convert a list into a tuple
marks=[50,56,67,89]
print(tuple(marks))
#Check the type of value stored in variable data = True
data = True
print(type(data))
#Take a string and print its length
city1="the name of city where we live is mahra"
print(len(city1))
#Print the first and last character of a string
print(city1[0],city1[-1])
#Convert any string to uppercase
print(city1.upper())
#Replace “a” with “@” in a given string.
print(city1.replace("a","@"))
#Count the number of words in a sentence
sentence=input("enter the sentence:")
words=sentence.split()
word_count=len(words)
print("number of words:",word_count)
#Check if a string contains the word “python”.
print("python"in sentence)
#Take a string and reverse it.
print(sentence[::-1])
#Check if the string starts with “hello”.
print(sentence.startswith("hello"))
#Take a user input string and print every second character.
print(sentence[::2])
#print if the number is even or odd?
num=int(input("enter the number:"))
if num %2==0:
    print("number is even")
else:
    print("number is odd")
#Ask the user’s age and check if they are adult (18+).
age=int(input("Enter the age of a person:"))
if age>=18:
    print("the person is adult")
else:
    print("the person is not adult")
    