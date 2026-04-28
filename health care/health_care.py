import numpy as np

name,age,hospital,billing_amount=np.genfromtxt('health care\healthcare_dataset.csv',delimiter=',', usecols=(0,1,8,10), unpack=True, dtype=None,skip_header=1)
print(name)
print(age)
print(hospital)
print(billing_amount)

# hospital billing_amount  - statistics operations
print("hospital billing_amount mean: " , np.mean(billing_amount))
print("hospital billing_amount average: " , np.average(billing_amount))
print("hospital billing_amount std: " , np.std(billing_amount))
print("hospital billing_amount mod: " , np.median(billing_amount))
print("hospital billing_amount percentile - 25: " , np.percentile(billing_amount,25))
print("hospital billing_amount percentile  - 75: " , np.percentile(billing_amount,75))
print("hospital billing_amount percentile  - 3: " , np.percentile(billing_amount,3))
print("hospital billing_amount min : " , np.min(billing_amount))
print("hospital billing_amount max : " , np.max(billing_amount))

# hospital billing_amount  - maths operations
print("hospital billing_amount square: " , np.square(billing_amount))
print("hospital billing_amount sqrt: " , np.sqrt(billing_amount))
print("hospital billing_amount pow: " , np.power(billing_amount,billing_amount))
print("hospital billing_amount abs: " , np.abs(billing_amount))


# Perform basic arithmetic operations
addition = billing_amount + age
subtraction = billing_amount - age
multiplication = billing_amount * age
division = billing_amount / age

print("billing_amount - age  - Addition:", addition)
print(" billing_amount - age - Subtraction:", subtraction)
print(" billing_amount - age - Multiplication:", multiplication)
print("billing_amount - age - Division:", division)



#Trigonometric Functions

billing_amountPie = (billing_amount/np.pi) +1

# Calculate sine, cosine, and tangent
sine_values = np.sin(billing_amountPie)
cosine_values = np.cos(billing_amountPie)
tangent_values = np.tan(billing_amountPie)

print("hospital billing_amount - div - pie  - Sine values:", sine_values)
print("hospital billing_amount - div - pie Cosine values:", cosine_values)
print("hospital billing_amount - div - pie Tangent values:", tangent_values)

print("hospital billing_amount - div - pie  - Exponential values:", np.exp(billing_amountPie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(billing_amountPie)
log10_array = np.log10(billing_amountPie)

print("hospital billing_amount - div - pie  - Natural logarithm values:", log_array)
print("hospital billing_amount - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(billing_amountPie)
print("hospital billing_amount - div - pie   - Hyperbolic Sine values:", sinh_values)

#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(billing_amountPie)
print("hospital billing_amount - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(billing_amountPie)
print("hospital billing_amount - div - pie   -Hyperbolic Tangent values:", tanh_values)

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(billing_amountPie)
print("hospital billing_amount - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(billing_amountPie)
print("hospital billing_amount - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)

#Zameen.com Long Plus Lat - 2 dimentional arrary
D2age_billing_amount = np.array([billing_amount,age])

print ("Zameen.com Long Plus Lat - 2 dimentional arrary - " ,D2age_billing_amount)

# check the dimension of array1
print("Zameen.com Long Plus Lat - 2 dimentional arrary - dimension" , D2age_billing_amount.ndim) 
# Output: 2

# return total number of elements in array1
print("Zameen.com Long Plus Lat - 2 dimentional arrary - total number of elements" ,D2age_billing_amount.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("Zameen.com Long Plus Lat - 2 dimentional arrary - gives size of array in each dimension" ,D2age_billing_amount.shape)
# Output: (2,3)

# check the data type of array1
print("Zameen.com Long Plus Lat - 2 dimentional arrary - data type" ,D2age_billing_amount.dtype) 
# Output: int64