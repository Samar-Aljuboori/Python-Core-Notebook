#Python Strings
#-------------------------------------------------------------------
# 1.  created a string
#----------------------
# using double quotes ---> "   "
string1 = "Python"

# using single quotes ---> '   '
string1 = 'Python'


# Multiline String
#------------------ 
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)              # Output : Never gonna give you up
                            #          Never gonna let you down


#-----------------------------------------------------------------------------------------------
# 2. Three ways  to access String Characters in Python 
#--------------------------------------

# 2.1 Indexing:    ---> [Index Number]  
#------------------------------------
name = "Samar"
print(name[0])              # Output: S


# 2.2 Negative Indexing  ---> [- Index Number]
#--------------------------------------------
name = "Samar"
print(name[-1])             # Output: r (Last letter)


# 3.2 Slicing:  ---> [Start:End]
#------------------------------
name = "Samar"
print(name[0:3])             # Output: Sam

#Note: If we try to access an index out of the range or use numbers other than an integer,we will get errors.


#-----------------------------------------------------------------------------------------------
# 3. Python Strings are Immutable
#--------------------------------
message = 'Hello  Python'
message[0] = 'H'
print(message)             # Output:  TypeError: 'str' object does not support item assignment


# Assign the variable name to a new string
#-----------------------------------------
message = 'Hello  Python'

# assign new string to message variable
message = 'Hello World'

print(message);                   # Output: "Hello World"



#-----------------------------------------------------------------------------------------------
# 4. Python String Operations
#------------------------------
# A) Compare Two Strings  ---> (==)

str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)                     # False

# compare str1 and str3
print(str1 == str3)                     # True


# B) Join Two or More Strings
#----------------------------
greet = "Hello, "
name = "World"

# using + operator
result = greet + name
print(result)                    # Output: Hello, World


#-----------------------------------------------------------------------------------------------
# 5. Iterate Through a Python String using --->  for loop
word = 'Python'

# iterating through greet string
for letter in word:
    print(letter)              # P
                               # y
                               # t
                               # h
                               # o
                               # n


#-----------------------------------------------------------------------------------------------
# 6. Python String Length
#------------------------
word = 'Python'

# count length of greet string
print(len(word))                 # Output: 6


# We can test if a substring exists within a string or not, using the keyword  --->  in or not in
print('o' in 'word')               # Output: True
print('py' not in 'python')        #  Output: False

#------------------------------------------------------------------------------------------------
# 7. Python String Formatting ---> (f-Strings)
#---------------------------------------------
name = 'Samar'
age = '29'

print(f'Hi, i am {name} and i am {age} years old')


#-----------------------------------------------------------------------------------------------
# 8. Comprehensive Examples of Core String Methods
#----------------------------------------------

#  a base string for our examples:
course = "  Python Developer Course  "
print(f"Original String: '{course}'\n")

# 1.8 Converts the entire string to uppercase  ---> upper()
print(f"1. upper(): '{course.upper()}'")                    # Output: '  PYTHON DEVELOPER COURSE  '

# 2.8 Converts the entire string to lowercase  ---> lower() 
print(f"2. lower(): '{course.lower()}'")                     # Output: '  python developer course  '

# 3.8 Splits the string at the first occurrence of a separator   ---> partition() 
# and returns a tuple with 3 elements:   (before, separator, after)
sample_text = "Samar-Python-Developer"
print(f"3. partition('-'): {sample_text.partition('-')}")     # Output: ('Samar', '-', 'Python-Developer')

# 4.8 Replaces a specific substring with another substring  ---> replace()
print(f"4. replace('Course', 'Bootcamp'): '{course.replace('Course', 'Bootcamp')}'")  # Output: 4. replace('Course', 'Bootcamp'): '  Python Developer Bootcamp  '

# 5.8 Returns the index of the first occurrence of a substring  ---> find() 
# Returns -1 if the substring is not found.
print(f"5. find('Developer'): {course.find('Developer')}")      # Output: 5. find('Developer'): 9

# 6.8 Removes any trailing characters (spaces or specific characters) from the right side  ---> rstrip() 
print(f"6. rstrip(): '{course.rstrip()}'")                      # Output: 6. rstrip(): '  Python Developer Course'

# 7.8 Splits the string from the left based on a separator and returns a List  ---> split()
clean_text = "Python Developer Course"
print(f"7. split(' '): {clean_text.split(' ')}")                # Output: ['Python', 'Developer', 'Course']

# 8.8 Checks if the string starts with a specified value (Returns True/False)  ---> startswith()
# Note: We use strip() first to remove spaces before checking
print(f"8. startswith('Python'): {course.strip().startswith('Python')}") # Output: True

# 9.8 Checks if all characters in the string are numeric characters  --->  isnumeric()
age_string = "29"
print(f"9. isnumeric() for '29': {age_string.isnumeric()}")              # Output: True
print(f"   isnumeric() for 'Samar': {'Samar'.isnumeric()}")              # Output: False

# 10.8 Returns the index of a substring (Similar to find, but raises an Error if not found)  ---> index() 
print(f"10. index('Python'): {clean_text.index('Python')}")              # Output: 0


#----------------------------------------------------------------------------------------------------
# 9. The method returns the string representation of a given object ---> str()

# string representation of Samar
name = str('Samar')
print(name)

# string representation of an integer 40
age = str(29)
print(age)

# string representation of a numeric string 162 cm
height = str('162 cm')
print(height)


# Other example to str()

age = 29       #(Integer Value)  
# If we try to concatenate a number with a string directly,
#  an error will occur; therefore, we convert it using str().
message = "I am " + str(age) + " years old."
print(message)              # Output: I am 29 years old.       # 29 now is String Value


#-----------------------------------------------------------------------------------------------
# 10. Escape Characters (Special Symbols)
#-----------------------------------------------------------------------------------------------
# Using \n for a new line and \" to print quotes inside a string
escaped_text = "Hello,\nWelcome to \"Python Developer\" guide."
print(escaped_text)                # Output:
                                   # Hello,
                                   # Welcome to "Python Developer" guide.


#-----------------------------------------------------------------------------------------------
# 11. Alternative String Formatting ---> .format() method
#-----------------------------------------------------------------------------------------------
# This is the older way before f-strings, you will see it often in legacy code
template = "Hi, my name is {} and I am {} years old."
formatted_text = template.format("Samar", 29)
print(formatted_text)      # Output: Hi, my name is Samar and I am 29 years old.