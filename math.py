# =====================================================================
# PYTHON MATH 
# =====================================================================

# 1. Basic Arithmetic Operators (Built-in)
# You don't need to import anything to use these:

sum_result = 10 + 5       # Addition (+)          -> 15
sub_result = 10 - 5       # Subtraction (-)       -> 5
mult_result = 10 * 5      # Multiplication (*)    -> 50
div_result = 10 / 3       # Normal Division (/)   -> 3.3333333333333335
floor_div = 10 // 3       # Floor Division (//)   -> 3 (Removes decimals)
mod_result = 10 % 3       # Modulus (%)           -> 1 (Remainder of division)
power_result = 2 ** 3     # Exponentiation (**)   -> 8 (2 to the power of 3)


# =====================================================================
# 2. The Built-in Math Functions
# =====================================================================

absolute = abs(-7)        # Returns absolute value -> 7
power_func = pow(2, 3)    # Same as 2 ** 3         -> 8
lowest = min(5, 10, 3)    # Finds lowest value    -> 3
highest = max(5, 10, 3)   # Finds highest value   -> 10
rounded = round(3.75, 1)  # Rounds to 1 decimal   -> 3.8


# =====================================================================
# 3. The "math" Module (Advanced Mathematics)
# To use these, you must write 'import math' at the very top.
# =====================================================================
import math

# Rounding Functions
round_up = math.ceil(4.2)     # Ceil   -> Rounds UP to nearest integer (5)
round_down = math.floor(4.9)  # Floor  -> Rounds DOWN to nearest integer (4)

# Roots and Logarithms
square_root = math.sqrt(64)   # Square Root -> 8.0
factorial_num = math.factorial(5) # 5! -> 5 * 4 * 3 * 2 * 1 = 120

# Constants
pi_value = math.pi            # Pi constant (~3.14159)
e_value = math.e              # Euler's number (~2.71828)


