# =================================================================
# Lambda Functions (Anonymous Functions) In Python
# =================================================================

# 1. Simple Lambda with one argument
# Takes 'x' and adds 5 to it
add_five = lambda x: x + 5

# 2. Lambda with multiple arguments
# Takes 'a' and 'b' and multiplies them
multiply = lambda a, b: a * b

# Caling Function:
print("=== Step 1: Basic Lambdas ===")
print(f"Result of add_five(10): {add_five(10)}")        # Result of add_five(10): 15
print(f"Result of multiply(4, 5): {multiply(4, 5)}")    # Result of multiply(4, 5): 20
   

# =================================================================
# Practical Application with built-in functions
# =================================================================

# A list of grades
grades = [45, 88, 92, 50, 64, 75]

# Using Lambda with filter() to get passing grades (>= 50)
passing_grades = list(filter(lambda score: score >= 50, grades))

# Caling Function:
print("=== Step 2: Lambda with filter() ===")
print(f"Original grades: {grades}")             # Original grades: [45, 88, 92, 50, 64, 75]
print(f"Passing grades only: {passing_grades}") # Passing grades only: [88, 92, 50, 64, 75]


# =================================================================

# Using Lambda with map() to add a 5-point bonus to every grade
grades = [45, 88, 92, 50, 64, 75]
bonus_grades = list(map(lambda score: score + 5, grades))

# Caling Function:
print("=== Step 3: Lambda with map() ===")
print(f"Grades after adding +5 bonus: {bonus_grades}")
# Grades after adding +5 bonus: [50, 93, 97, 55, 69, 80]

