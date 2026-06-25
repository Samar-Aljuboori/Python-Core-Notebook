#Python Numbers
#---------------------------------------------------------------------------
#Variables of numeric types are created when you assign a value to them:
#-----------------------------------------------------------------------
x = 65    # int
y = 2.3  # float
z = 1j   # complex

# To verify the type of any object in Python, use ---> type() function
print(type(x))        # Output : int
print(type(y))        # Output : float
print(type(z))        # Output : complex


#-------------------------------------------------------------------------------------------------
# 1. Integers: 
#-------------
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 35656222554887711
z = -3255522

print(type(x))        # Output: <class 'int'>
print(type(y))        # Output: <class 'int'>
print(type(z))        # Output: <class 'int'>


#----------------------------------------------------------------------------------------------------
# 2. Floats :
#-----------
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59

print(type(x))         # Output: <class 'float'>
print(type(y))         # Output: <class 'float'>
print(type(z))         # Output: <class 'float'>


#----------------------------------------------------------------------------------------------------

# 3. Complex:
#---------
# Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))        # Output: <class 'complex'>
print(type(y))        # Output: <class 'complex'>
print(type(z))        # Output: <class 'complex'>

#----------------------------------------------------------------------------------------------------

# 4. Type Conversion :
#--------------------
# You can convert from one type to another with the int(), float(), and complex() methods:
#------------------------------------------------------------------------------------------

# Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)                             # Output : 1.0
print(b)                             # Output : 2
print(c)                             # Output : (1+0j)

print(type(a))                       # Output : <class 'float'>
print(type(b))                       # Output : <class 'int'>
print(type(c))                       # Output : <class 'complex'>


#------------------------------------------------------------------------------------------
######### Note: You cannot convert complex numbers into another number type.#########
#------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------
# 5. Random Number :
#-----------------
# Python does not have a random() function to make a random number, but Python has a built-in module called random 
# that can be used to make random numbers:

#Import the random module, and display a random number from 1 to 9:

import random

print(random.randrange(1, 10))          # Output: A random number between 1 and 9 (e.g., 5)



#----------------------------------------------------------------------------------------------------
# 6. Scientific Numbers (Floats with 'e')
#----------------------------------------------------------------------------------------------------
# 'e' or 'E' indicates the power of 10.
sci1 = 35e3   # 35 * 10^3 = 35000.0
sci2 = 12E4   # 12 * 10^4 = 120000.0

print(type(sci1))                     # Output: <class 'float'>
print(sci1)                           # Output: 35000.0


#----------------------------------------------------------------------------------------------------
# 7. Advanced Arithmetic Operations
#----------------------------------------------------------------------------------------------------
num1 = 10
num2 = 3

print(num1 / num2)   # Normal Division                          Output: 3.3333333333333335
print(num1 // num2)  # Floor Division (ignores decimals)        Output: 3
print(num1 % num2)   # Modulus (Remainder of division)          Output: 1
print(num1 ** num2)  # Exponentiation (10 to the power of 3)    Output: 1000


#----------------------------------------------------------------------------------------------------
# 8. Built-in Math Functions
#----------------------------------------------------------------------------------------------------
negative_num = -5.75

# abs() returns the absolute (positive) value of a number
print(abs(negative_num))              # Output: 5.75

# round() rounds a floating-point number to a specified number of decimals (default is 0)
print(round(negative_num))            # Output: -6
print(round(3.14159, 2))              # Output: 3.14


