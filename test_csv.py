
import numpy as np

ids,status,price,city = np.genfromtxt(
    r"C:\Users\hp\OneDrive\Documents\GitHub\AI-Course-Bin\RealEstate-USA.csv",
    delimiter=",",
    usecols=(0,1,2,7),
    unpack=True,
    dtype=None,
    skip_header=1
)

print(ids)
print(status)
print(price)
print(city)


# RealEstateUSA.COM price  - statistics operations
print("RealEstateUSA.COM Price mean: " , np.mean(price))
print("RealEstateUSA.COM Price average: " , np.average(price))
print("RealEstateUSA.COM std: " , np.std(price))
print("RealEstateUSA.COM Price mod: " , np.median(price))
print("RealEstateUSA.COM Price percentile - 25: " , np.percentile(price,25))
print("RealEstateUSA.COM percentile  - 75: " , np.percentile(price,75))
print("RealEstateUSA.COM Price percentile  - 3: " , np.percentile(price,3))
print("RealEstateUSA.COM Price min : " , np.min(price))
print("RealEstateUSA.COM Price max : " , np.max(price))

#  price  - maths operations
print("RealEstateUSA.COM Price square: " , np.square(price))
print("RealEstateUSA.COM Price sqrt: " , np.sqrt(price))
print("RealEstateUSA.COM Price pow: " , np.power(price,price))
print("RealEstateUSA.COM Price abs: " , np.abs(price))


#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("RealEstateUSA.COM Price - div - pie  - Sine values:", sine_values)
print("RealEstateUSA.COM - div - pie Cosine values:", cosine_values)
print("RealEstateUSA.COM Price - div - pie Tangent values:", tangent_values)

print("RealEstateUSA.COM Price - div - pie  - Exponential values:", np.exp(pricePie))



#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("Zameen.com Price - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print(" RealEstateUSA.COM Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("RealEstateUSA.COM Price - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("RealEstateUSA.COM Price - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("RealEstateUSA.COM Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)
