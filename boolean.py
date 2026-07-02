# Booleans In Python (True / False Evaluation)
#---------------------------------------------------------------------------------------
# 1. Boolean Values & Expressions
#---------------------------------------------------------------------------------------
# Booleans represent one of two values: True or False. 
# In Python, they must always start with a capital letter.

is_game_over = False
is_user_logged_in = True

print("1.1 Boolean Types:", type(is_user_logged_in)) # Output: <class 'bool'>

# Evaluating expressions returns Booleans automatically
print("1.2 Expression evaluation (10 > 9):", 10 > 9)   # Output: True
print("1.3 Expression evaluation (10 == 9):", 10 == 9) # Output: False


#---------------------------------------------------------------------------------------
# 2. Comparison Operators Returning Booleans
#---------------------------------------------------------------------------------------
car_speed = 120
speed_limit = 100

is_speeding = car_speed > speed_limit
is_exact_limit = car_speed == speed_limit

print("\n2.1 Is speeding?:", is_speeding)      # Output: True
print("2.2 Is exact limit?:", is_exact_limit)  # Output: False


#---------------------------------------------------------------------------------------
# 3. The bool() Function & Truthy vs Falsy Values
#---------------------------------------------------------------------------------------
# Almost any value is evaluated to True if it has some sort of content.

# 3.1 Truthy Values (Evaluates to True)
print("\n3.1 Truthy Examples:")
print(" - Non-empty string:", bool("Hello"))    # True
print(" - Any number except 0:", bool(42))      # True
print(" - Any non-empty list:", bool(["apple"])) # True

# 3.2 Falsy Values (Evaluates to False)
# Python has very specific values that resolve to False:
print("\n3.2 Falsy Examples (All return False):")
print(" - False itself:", bool(False))
print(" - None value:", bool(None))
print(" - Integer zero:", bool(0))
print(" - Float zero:", bool(0.0))
print(" - Empty string:", bool(""))
print(" - Empty list:", bool([]))
print(" - Empty tuple:", bool(()))
print(" - Empty dictionary:", bool({}))

# Output : 3.2 Falsy Examples (All return False):
 #          - False itself: False
 #          - None value: False
 #          - Integer zero: False
 #          - Float zero: False
 #          - Empty string: False
 #          - Empty list: False
 #          - Empty tuple: False
 #          - Empty dictionary: False


#---------------------------------------------------------------------------------------
# 4. Logical Operators (and, or, not)
#---------------------------------------------------------------------------------------
has_premium_account = True
has_discount_coupon = False

# and: True if both are True
print("\n4.1 Using 'and':", has_premium_account and has_discount_coupon) # Output : False

# or: True if at least one is True
print("4.2 Using 'or':", has_premium_account or has_discount_coupon)   # Output : True

# not: Reverses the boolean value
print("4.3 Using 'not':", not has_premium_account)                      # Output : False


#---------------------------------------------------------------------------------------
# 5. Functions Returning Booleans & Built-in checks
#---------------------------------------------------------------------------------------
def is_even(number):
    return number % 2 == 0

print("\n5.1 Custom function check (is 4 even?):", is_even(4)) # Output: True

# Built-in isinstance() function returns a boolean
text_value = "Stuttgart"
print("5.2 Is 'text_value' a string?:", isinstance(text_value, str)) # Output: True
print("5.3 Is 'text_value' an integer?:", isinstance(text_value, int)) # Output: False