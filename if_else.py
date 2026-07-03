# Conditional Statements In Python (if, elif, else)
#---------------------------------------------------------------------------------------
# 1. Basic Single Condition (if) & The Indentation Rule
#---------------------------------------------------------------------------------------
# Python relies on indentation (white space at the beginning of a line) to define scope.
# Colons (:) are mandatory after every conditional statement.

temperature = 25

print("1. Testing Single If:")    # Output : 1. Testing Single If:
if temperature > 20:
    print(" - It is a warm day!") # Executed because condition is True

# Output :  - It is a warm day!


#---------------------------------------------------------------------------------------
# 2. Dual Path Condition (if...else)
#---------------------------------------------------------------------------------------
# The 'else' keyword catches anything which isn't caught by the preceding conditions.

car_speed = 110
speed_limit = 100

print("\n2. Testing If...Else:")    # Output : 2. Testing If...Else:
if car_speed <= speed_limit:
    print(" - Driving safely.")
else:
    print(" - Warning: You are speeding!") # Executed

# Output :  - Warning: You are speeding!



#---------------------------------------------------------------------------------------
# 3. Multiple Conditions (if...elif...else)
#---------------------------------------------------------------------------------------
# 'elif' is Python's way of saying "if the previous conditions were not true, then try this".

score = 85

print("\n3. Testing If...Elif...Else Chain:")     # Output : 3. Testing If...Elif...Else Chain:
if score >= 90:
    print(" - Grade: Elite / Excellent")
elif score >= 80:
    print(" - Grade: Professional / Very Good") # Executed
elif score >= 70:
    print(" - Grade: Good")
else:
    print(" - Grade: Needs Improvement")

# Output :  - Grade: Professional / Very Good



#---------------------------------------------------------------------------------------
# 4. Nested Conditions (If inside If)
#---------------------------------------------------------------------------------------
# Conditional statements can be nested inside another to fulfill deeper structural logic.

is_logged_in = True
has_premium_access = False

print("\n4. Testing Nested If Structure:")    # Output : 4. Testing Nested If Structure:
if is_logged_in:
    print(" - User session validated.")       # Output :  - User session validated.
    if has_premium_access:
        print(" - Access Granted: Displaying premium tools dashboard.")
    else:
        print(" - Access Limited: Please upgrade to Premium.")  # Exected
else:
    print(" - Access Denied: Please log in first.")

# Output :  - Access Limited: Please upgrade to Premium.



#---------------------------------------------------------------------------------------
# 5. Logical Operators inside Conditions (and, or)
#---------------------------------------------------------------------------------------
# 5.1 The 'and' operator requires ALL sub-conditions to be True
has_html_skill = True
has_react_skill = True

print("\n5.1 Testing 'and' Condition:")       # Output : 5.1 Testing 'and' Condition:
if has_html_skill and has_react_skill:
    print(" - Status: Qualified for Full-Stack Frontend developer role.")  # Exected
else:
    print(" - Status: Missing required skills.")

# Output :  - Status: Qualified for Full-Stack Frontend developer role.


# 5.2 The 'or' operator requires at least ONE sub-condition to be True
is_weekend = False
is_holiday = True

print("5.2 Testing 'or' Condition:")       # Output : 5.2 Testing 'or' Condition:
if is_weekend or is_holiday:
    print(" - Status: Office is closed.") 
else:
    print(" - Status: Standard working day.")

# Output :  - Status: Office is closed.



#---------------------------------------------------------------------------------------
# 6. Short Hand Conditions (Ternary Operator / One-Liners)
#---------------------------------------------------------------------------------------
# If you have only one statement to execute, one for if, and one for else, you can put it all on one line.

age = 29
print("\n6. Short Hand Execution:")      # Output : 6. Short Hand Execution:

# Syntax: [Statement_if_True] if [Condition] else [Statement_if_False]
user_status = "Adult Profile" if age >= 18 else "Minor Profile"
print(" - Result:", user_status)     
 # Output :  - Result: Adult Profile




#---------------------------------------------------------------------------------------
# 7. The 'pass' Statement Placeholder
#---------------------------------------------------------------------------------------
# 'if' statements cannot be empty. If you want to keep it empty for future code, use 'pass'.

x = 50
y = 200

print("\n7. Pass placeholder executed:")      # Output : 7. Pass placeholder executed:
if y > x:
    pass # No error will be thrown. Python skips smoothly.
print(" - Passed successfully.")      # Output :  - Passed successfully.