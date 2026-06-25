# Variables In Python
#---------------------------------------------------------------------------------------
# 1. Variable Naming Rules (Legal vs Illegal)
#---------------------------------------------------------------------------------------

# 1.1 Legal variable names:
myvar = "Python"
my_var = "Python"
_my_var = "Python"
myVar = "Python"
MYVAR = "Python"
myvar2 = "Python"

# 1.2 Illegal variable names (Commented out to prevent SyntaxError):
# 2mystr = "Python"   # Cannot start with a number
# my-str = "Python"   # Cannot contain hyphens
# my str = "Python"   # Cannot contain spaces


#---------------------------------------------------------------------------------------
# 2. Variable Naming Cases (Clean Code Best Practices)
#---------------------------------------------------------------------------------------

# Multi-word variable names can be written in different professional formats:

# A) Camel Case: Each word, except the first, starts with a capital letter
myVariableName = "Samar"

# B) Pascal Case: Each word starts with a capital letter
MyVariableName = "Samar"

# C) Snake Case: Words are separated by underscores (Recommended for Python!)
my_variable_name = "Samar"


#---------------------------------------------------------------------------------------
# 3. Case-Sensitivity
#---------------------------------------------------------------------------------------
# Variable names are case-sensitive. Capital letters create completely different variables.
a = 4
A = "Samar" 

print(a)                              # Output: 4
print(A)                              # Output: Samar (A will not overwrite a)


#---------------------------------------------------------------------------------------
# 4. Modifying Variables & Dynamic Typing
#---------------------------------------------------------------------------------------
# You can change the value and even the data type of a variable at any time.
text = 'Hello World'
print(text)                           # Output: Hello World

# Assigning a new value to the same variable
text = 'Hello Python'
print(text)                           # Output: Hello Python


#---------------------------------------------------------------------------------------
# 5. Multiple Assignments
#---------------------------------------------------------------------------------------

# 5.1 Assigning many values to multiple variables in one line:
x, y, z = 4.5, 22, 'Python'
print(x)                              # Output: 4.5
print(y)                              # Output: 22
print(z)                              # Output: Python 

# 5.2 Assigning the exact same value to multiple variables at once:
skill1 = skill2 = 'Python'
print(skill1)                         # Output: Python 
print(skill2)                         # Output: Python 


#---------------------------------------------------------------------------------------
# 6. Basic Core Data Types (Quick Overview)
#---------------------------------------------------------------------------------------
# Variables can hold different types of data. Detailed guides are in separate files.

# Text Type (String - can use single or double quotes)
text_sample = "This is a string"

# Numeric Types
integer_num = 10                      # <class 'int'>
float_num = 12.8                      # <class 'float'>

# Boolean Type
is_pass = True                        # <class 'bool'>

# None Type (Represents the absence of a value)
empty_value = None
print(empty_value)                    # Output: None