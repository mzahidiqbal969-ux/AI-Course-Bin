l=[1,9,8,4,3,6,7]
l.append(170)
print(l)
l.remove(3)
print(l)
#Sort a list in ascending order.
l.sort()
print(l)
#Print the first and last elements of a list
print(l[0])
print(l[6])
#Create a tuple of 5 names and print the third one.
t=("ali","zain","zaki","javed","zahid")
print(t[2])
#Convert a tuple into a list
print(list(t))
print(type(list(t)))
#Find how many times an element appears in a list.
print(l.count(2))
#Create a list of numbers and print only even numbers
for n in l:
    if n%2==0:
        print(n)
#Join two lists into one
l2=[2,5,9,6,7,0]
l3=l+l2
print(l3)
#Print numbers from 1 to 20 using a for loop
for i in range(1,21):
    print(i)
#Print multiples of 5 from 1 to 50
for i in range(1,51):
    if i%5==0:
        print(i)
#Print the table of a number entered by the user
num=int(input("Enter any number:"))
