newspaper_id=45
print(newspaper_id)
print(type(newspaper_id))
newspapertitle="dawn"
print(newspapertitle)
print(type(newspapertitle))
newspaperprice=34.5
ns=newspaperprice+5
print(ns)
print(ns/2)
print(newspaperprice)
print(type(newspaperprice))
editor=input("enter editor name:")
print("hello editor: "+editor)
#print("upper:",+ editor.upper())
newseditorname="zahid"
for i in "zahid":
    print(i)
print(len(newseditorname))
if newspaperprice>50:
    print("value greater than 50")
elif newspaperprice<50:
    print("value is less than 50")
else:
    print("value is same")
if newspaper_id<30 and newspaperprice>20:
    print("true value 1")
if newspaper_id<30 or newspaperprice>20:   
    print("true value2")
d={"pakistan":"islamabad","india":"dehli","srilanka":"colombo"}
print(d)
print(type(d))
d["saudi arabia"]="riaz"
print(d)
del d["india"]
print(d)
# d.clear()
# print(d)
for country in d:
    print(d)
    print(country)
    print(d[country])
z=[1,3,6,8,9]
z.append("z")
print(z)
z1=[4,5,2,1]
z1.sort()
print(z1)
z1.remove(5)
print(z1)
z1.index(1)
print(z1)

fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])   # "apple" (first element)
print(fruits[2])   # "cherry" (third element)

print(fruits[-1])  # "date"
print(fruits[-2])  # "cherry"

numbers = [10, 20, 30, 40, 50]
pos = numbers.index(30)
print(pos)   # 2 (because 30 is at index 2)

print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[-2:])   # ['cherry', 'date']
z2=[2,1,4,5,7,6]
z2.extend(2)
print(z2)
