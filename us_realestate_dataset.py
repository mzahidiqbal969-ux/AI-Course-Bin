import numpy as np
ids,status,price,city=np.genfromtxt(r'C:\Users\hp\OneDrive\Documents\GitHub\AI-Course-Bin\RealEstate-USA.csv',delimiter=',',usecols=(0,1,2,7),unpack=True,dtype=None,skip_header=1)
print(ids)
print(status)
print(price)
print(city)
# import os
# import os

# path = r'C:\Users\hp\OneDrive\Documents\GitHub\AI-Course-Bin\RealEstate-USA.csv'
# print(os.path.exists(path))
# import os
# print(os.path.exists(r'C:\Users\hp\OneDrive\Documents\GitHub\AI-Course-Bin\RealEstate-USA.csv'))


# ids, status, price, city = np.genfromtxt(
#     r"C:\Users\hp\OneDrive\Documents\GitHub\AI-Course-Bin\RealEstate-USA.csv",
#     delimiter=",",
#     usecols=(0,1,2,7),
#     unpack=True,
#     dtype=None,
#     skip_header=1
# )

# print(ids)
# print(status)
# print(price)
# print(city)




