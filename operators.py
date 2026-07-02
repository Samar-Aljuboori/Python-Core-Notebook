# All  Operators In Python (7 Groups Complete)
#---------------------------------------------------------------------------------------
# 1. Arithmetic Operators
#---------------------------------------------------------------------------------------
# Used with numeric values to perform common mathematical operations.

x = 10
y = 3

print("1.1 Addition (+):", x + y)          # 13
print("1.2 Subtraction (-):", x - y)       # 7
print("1.3 Multiplication (*):", x * y)    # 30
print("1.4 Division (/):", x / y)          # 3.3333333333333335 (Always float)
print("1.5 Modulus (%):", x % y)           # 1 (Remainder of the division)
print("1.6 Exponentiation (**):", x ** y)  # 1000 (10 to the power of 3)
print("1.7 Floor Division (//):", x // y)  # 3 (Rounds down to nearest whole number)


#---------------------------------------------------------------------------------------
# 2. Assignment Operators
#---------------------------------------------------------------------------------------
# Used to assign and update values to variables efficiently.

num = 5
num += 3  # Equivalent to: num = num + 3 -> 8
num *= 2  # Equivalent to: num = num * 2 -> 16
num //= 4 # Equivalent to: num = num // 4 -> 4
print("\n2. Final Assignment Value:", num)    # Output : 2. Final Assignment Value: 4


#---------------------------------------------------------------------------------------
# 3. Comparison Operators
#---------------------------------------------------------------------------------------
# Compare two values and always return a Boolean (True/False).

a = 20
b = 10

print("\n3.1 Equal to (==):", a == b)       # False
print("3.2 Not equal to (!=):", a != b)    # True
print("3.3 Greater than (>):", a > b)       # True
print("3.4 Less than (<):", a < b)          # False
print("3.5 Greater than or equal (>=):", a >= 20) # True


#---------------------------------------------------------------------------------------
# 4. Logical Operators
#---------------------------------------------------------------------------------------
# Used to combine conditional statements.

is_admin = True
is_verified = False

print("\n4.1 Logical 'and':", is_admin and is_verified) # False (Both must be True)
print("4.2 Logical 'or':", is_admin or is_verified)   # True (At least one must be True)
print("4.3 Logical 'not':", not is_admin)               # False (Reverses the expression)


#---------------------------------------------------------------------------------------
# 5. Identity Operators (is, is not)
#---------------------------------------------------------------------------------------
# Compare the memory locations of two objects, not just their content.

list_one = ["HTML", "CSS"]
list_two = ["HTML", "CSS"]
list_three = list_one

print("\n5.1 Value Comparison (==):", list_one == list_two) # True (Content is identical)
print("5.2 Object Identity (is):", list_one is list_two)   # False (Different locations in memory)
print("5.3 Object Identity (is):", list_one is list_three) # True (Points to the exact same object)


#---------------------------------------------------------------------------------------
# 6. Membership Operators (in, not in)
#---------------------------------------------------------------------------------------
# Used to test if a sequence/item is present in an object (list, string, dict, set).

stack = ["Python", "Django", "React", "MySQL"]

print("\n6.1 Member exists (in):", "Django" in stack)       # True
print("6.2 Member missing (not in):", "PHP" not in stack)  # True


#---------------------------------------------------------------------------------------
# 7. Bitwise Operators
#---------------------------------------------------------------------------------------
# Used to compare/manipulate (binary) numbers at the bit level.

bin_a = 6  # Binary: 0110
bin_b = 3  # Binary: 0011

print("\n7.1 Bitwise AND (&):", bin_a & bin_b)   # 2  (Binary: 0010)
print("7.2 Bitwise OR (|):", bin_a | bin_b)    # 7  (Binary: 0111)
print("7.3 Bitwise XOR (^):", bin_a ^ bin_b)   # 5  (Binary: 0101)
print("7.4 Bitwise NOT (~):", ~bin_a)          # -7 (Inverts all the bits)
print("7.5 Left Shift (<<):", bin_a << 1)      # 12 (Shifts bits left by 1 position)
print("7.6 Right Shift (>>):", bin_a >> 1)     # 3  (Shifts bits right by 1 position)