marks=int(input("Enter the marks: "))
if marks>=90:
    print("Grade A:")
elif marks>=80:
    print("Grade B:")
elif marks>=70:
    print("Grade C:")
elif marks>=60:
    print("Grade D:")
else:
    print("Grade F:")

m=int(input("Enter the month number: "))
if m==1:
    print("January")
elif m==2:
    print("February")
elif m==3:
    print("March")
elif m==4:
    print("April")
elif m==5:
    print("May")
elif m==6:
    print("June")
elif m==7:
    print("July")
elif m==8:
    print("August")
elif m==9:
    print("September")
elif m==10:
    print("October")
elif m==11:
    print("November")
elif m==12:
    print("December")
else:
    print("Wrong Selection,please enter right month number")
m=int(input("Enter the month number: "))
month=["January","February","March","April","May","June","July","August","September","October","November","December"]
if m >= 1 and m <= 12:
    print(month[m-1])
else:
    print("write proper month ")
n=int(input("Enter the number: "))
if n>=1:
    print("Positive")
elif n<0:
    print("Negative") 
else:
    print("Zero") 
c=input("Enter the colour name: ").strip()
if c=="Red":
    print("Stop")
elif c=="Yellow":
    print("Wait")
elif c=="Green":
    print("Go")
else:
    print("Write a correct colour")
s=int(input("Enter the salary: "))
if s>=50000:
    print("with bonus: ",s*0.10+s)
elif s>=30000:
    print("with bonus: ",s*0.07+s)
else:
    print("with bonus: ",s*0.05+s)
a=int(input("Enter the age: "))
if a<13:
    print("child")
elif a>=13 and a<=19:
    print("teen")
elif a>=20 and a<=59:
    print("adult")
else:
    print("senior")
t=int(input("Enter the temperature: "))
if t>40:
    print("extremely heat")
elif 30<= t <=40:
    print("hot")
elif 20<= t <=29:
    print("warm")
elif 10<= t <=19:
    print("cool")
else:
    print("cold")
u=int(input("Enter the unit: "))
if u<=100:
    print("free")
elif u<=300:
    print("5 per unit:",u*5)
else:
    print("10 per unit:",u*10)
p=int(input("Enter the price: "))
if p>=10000:
    print("luxury item")
elif p>=5000:
    print("expensive")
elif p>=2000:
    print("affordable")
else:
    print("cheap")