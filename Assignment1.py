#Question no.1 Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = (Celsius * 9/5) + 32) 
# celsius = float(input("Enter the Celsius temperature: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit:", fahrenheit)

# Question no.2 Calculate Area of a Rectangle 
# l=float(input("Enter the length: "))
# w=float(input("Enter the width: "))
# area=l*w
# print("Area of a Rectangle: ",area)

#Question no.3,Calculate Compound Interest 
#Use the formula: 
#CI = P * (1 + R/100)**T - P 
#Where P = principal, R = rate, T = time
# p=float(input("Enter the Principal Amount: "))
# r=float(input("Enter the Interest Rate %: "))
# t=float(input("Enter the Time Period in years: "))
# compound_interest=p*(1+r/100)**t-p
# print("Calculation of Compound Interest: ",compound_interest)

#Question no.4,Perimeter of a Rectangle - Take length and width as input and calculate the perimeter
# length=float(input("Enter the length: "))
# width=float(input("Enter the width: "))
# perimeter=2*(length+width)
# print("Value of Perimeter: ",perimeter)

# #Question no.5,Average of Three Numbers - Input three numbers and print their average. 
# num1=float(input("Enter the 1st number: "))
# num2=float(input("Enter the 2nd number: "))
# num3=float(input("Enter the 3rd number: "))
# average_3num=(num1+num2+num3)/3
# print("Average of three numbers is here: ",average_3num)

#Question no,6 Square and Cube of a Number - Ask the user for a number and display its square and cube
# num4=float(input("Enter the number: "))
# square_num=num4*num4
# print("Value of Square: ",square_num)
# cube_num=num4**3
# print("Value of Cube: ",cube_num)

#Question no.7,Distribute Items Equally - You have n candies and k students. Write a program to find: how many candies each student gets 
#how many are left
#Question no.8,calculate Profit or Loss Input cost price and selling price. Display either:Profit and amount, or Loss and amount, or No Profit No Loss 
# cost_price=int(input("Enter the cost price: "))
# selling_price=int(input("Enter the selling price: "))
# if selling_price>cost_price: 
#     profit=selling_price-cost_price
#     print("Profit: ", profit)
# elif selling_price<cost_price:
#     loss=cost_price-selling_price
#     print("Loss: ",loss)
# else:
#     print("no profit, no loss")

# Question no 9.Total Marks and Percentage 
# Input marks of 5 subjects. Print: 
#  Total marks 
#  Percentage 
#  Average
# marks1=int(input("Enter marks of English: "))
# marks2=int(input("Enter marks of Math: "))
# marks3=int(input("Enter marks of Physics: "))
# marks4=int(input("Enter marks of Chemistry: "))
# marks5=int(input("Enter marks of Biology: "))
# total_marks=500
# obtained_marks=marks1+marks2+marks3+marks4+marks5
# print("Total obtained Marks: ",obtained_marks)
# per_marks=obtained_marks/total_marks *100
# print("Percentage Marks: ", per_marks)
# average_marks=obtained_marks/5
# print("Average Marks: ",average_marks)

#QUESTION NO 10,Salary Calculator 
# Input basic salary. Calculate: 
#  HRA = 20% of basic 
#  DA = 15% of basic 
#  Total Salary = Basic + HRA + DA 

# basic_sa=int(input("Enter the basic salary: "))
# hra=(basic_sa*20)/100
# da=(basic_sa*15)/100
# total_salary=basic_sa+hra+da
# print(total_salary)

#QUESTION NO,11.Age in Months and Days 
# Input your age in years. Calculate and print age in: 
#  Months 
#  Days (approximate)
# years=int(input("Enter the year: "))
# months=12*years
# print("Total Months: ", months)
# days=12*years*30
# print("Total days: ",days)

#QUESTION NO,12. Currency Converter (USD to PKR),Input amount in USD. Convert using a fixed exchange rate.
# usd=int(input("Enter the usd: "))
# exchange_rate = 285
# pkr=usd*exchange_rate
# print("Amount in PKR: ",pkr)

#QUESTION NO,13.Sum of First N Natural Numbers 
# Input a number n, calculate sum of first n natural numbers. 
# Formula: sum = n * (n + 1) / 2 

# n=int(input("Enter the number: "))
# sum=n*(n+1)//2
# print("sum of all natural numbers: ",sum)

#QUESTION NO.14,Percentage of Correct Answers 
#Input total questions and correct answers, and calculate the percentage score. 
# q=int(input("Enter the total questions: "))
# a=int(input("Enter the correct answers: "))


# per_correct_an=(a/q)*100
# print("percentage of correct answers: ",per_correct_an)

#QUESTION NO,15.Speed, Distance, and Time 
#Input distance and time, and calculate speed.
# d=int(input("Enter the distance in meters : "))
# t=int(input("Enter the time in seconds: "))
# if t!=0:
#     speed=d/t
#     print("speed: ",speed,"m/s")
# else:
#     ("Calculation is wrong")

#QUESTION NO,16.Calculate Body Mass Index (BMI) 
#Input weight (kg) and height (m), then calculate: 
#BMI = weight / (height ** 2) 
# weight=float(input("Enter the WEIGHT IN KG : "))
# height=float(input("Enter the HEIGHT IN METERS : "))
# bmi=weight / (height ** 2) 
# print("Body Mass Index: ", bmi)

#QUESTION NO,17.Convert Minutes to Hours and Minutes 
#Input number of minutes and convert to hours and remaining minutes. 
#Example: 130 minutes → 2 hours 10 minutes 

minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours:", hours)
print("Remaining Minutes:", remaining_minutes)

 

