newspaperlist={45,"Dawn",34.5,True}
print(newspaperlist)
print(type(newspaperlist))
newspaperlist.discard(34.5)
print(newspaperlist)
newspaperlist.add(2)
print(newspaperlist)
for items in newspaperlist:
    print(items)