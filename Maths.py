import math

# Basic Mathematical Functions
x = -4.7
y = 15
print(f"math.ceil({x}) = {math.ceil(x)}")
print(f"math.floor({x}) = {math.floor(x)}")
print(f"math.fabs({x}) = {math.fabs(x)}")
print(f"math.factorial(5) = {math.factorial(5)}")
print(f"math.fmod(20, 3) = {math.fmod(20, 3)}")
print(f"math.gcd(60, 48) = {math.gcd(60, 48)}")

# Power and Logarithmic Functions
print(f"math.exp(1) = {math.exp(1)}")
print(f"math.log(10) = {math.log(10)}")
print(f"math.log10(100) = {math.log10(100)}")
print(f"math.pow(2, 3) = {math.pow(2, 3)}")
print(f"math.sqrt(16) = {math.sqrt(16)}")

# Trigonometric Functions
angle = math.pi / 4  # 45 degrees in radians
print(f"math.sin({angle}) = {math.sin(angle)}")
print(f"math.cos({angle}) = {math.cos(angle)}")
print(f"math.tan({angle}) = {math.tan(angle)}")
print(f"math.asin(1) = {math.asin(1)}")
print(f"math.acos(0) = {math.acos(0)}")
print(f"math.atan(1) = {math.atan(1)}")
print(f"math.degrees({angle}) = {math.degrees(angle)}")
print(f"math.radians(45) = {math.radians(45)}")

# Hyperbolic Functions
x = 1.0
print(f"math.sinh({x}) = {math.sinh(x)}")
print(f"math.cosh({x}) = {math.cosh(x)}")
print(f"math.tanh({x}) = {math.tanh(x)}")
print(f"math.asinh({x}) = {math.asinh(x)}")
print(f"math.acosh(2) = {math.acosh(2)}")
print(f"math.atanh(0.5) = {math.atanh(0.5)}")

# Special Functions
print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")
print(f"math.inf = {math.inf}")
print(f"math.nan = {math.nan}")

# Angle Conversion
radians = math.radians(180)
degrees = math.degrees(math.pi)
print(f"180 degrees to radians: {radians}")
print(f"π radians to degrees: {degrees}")
