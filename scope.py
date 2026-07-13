# ==============================================================================
# Variable Scope in Python
# Description: Examples of Global, Local, and Enclosing scopes.
# ==============================================================================



# ==============================================================================
#  (Scope Lifecycle):
# ==============================================================================
# 1. Functions (def): 
#    - Create a strict wall. 
#    - Variables created inside a function DIE as soon as the function ends.
#
# 2. Blocks (if / for / while): 
#    - Do NOT create a new scope in Python. 
#    - Variables created inside an 'if' or a 'loop' SURVIVE and can be 
#      accessed anywhere outside them (within the same file/function).
# ==============================================================================


# ------------------------------------------------------------------------------
# SECTION 1: Global Scope vs Local Scope
# ------------------------------------------------------------------------------

# This variable is GLOBAL (Visible everywhere)
x = "Global Variable"

def my_function():
    # This variable is LOCAL (Only visible inside this function)
    y = "Local Variable"
    print("Inside function:")
    print(x) # Works! Functions can read global variables.
    print(y) # Works! Functions can read their own local variables.

my_function()
# -> Output:
# Inside function:
# Global Variable
# Local Variable

print("-" * 40)

print("Outside function:")
print(x) # Works!
# -> Output: Outside function: Global Variable

# NOTE: Un-commenting the line below will crash the program!
# print(y) # -> NameError: name 'y' is not defined


# ------------------------------------------------------------------------------
# SECTION 2: Modifying Global Variables (The 'global' keyword)
# ------------------------------------------------------------------------------

print("\nSECTION 2: Using global keyword")

counter = 10

def increment_counter():
    global counter # Gives permission to modify the global 'counter'
    counter += 1

increment_counter()
print(f"Counter value: {counter}")
# -> Output: Counter value: 11

print("-" * 40)


# ------------------------------------------------------------------------------
# SECTION 3: Nested Functions (The 'nonlocal' keyword)
# ------------------------------------------------------------------------------

print("SECTION 3: Using nonlocal keyword")

def outer_function():
    message = "Outer Message"
    
    def inner_function():
        nonlocal message # Gives permission to modify the outer function's variable
        message = "Modified by Inner"
        print(f"Inner says: {message}")
        
    inner_function()
    print(f"Outer says: {message}")

outer_function()
# -> Output:
# Inner says: Modified by Inner
# Outer says: Modified by Inner


# ------------------------------------------------------------------------------
# SECTION 4: Loops and If-Statements DO NOT create a new scope!
# Variables created inside 'if' blocks or 'loops' are still accessible outside.
# ------------------------------------------------------------------------------

print("\nSECTION 4: Scope in Loops and If-statements")

if True:
    status_message = "Python is awesome!" # Created inside an IF block

# This works perfectly in Python! (In Java or C++, this would crash)
print(f"Outside IF block: {status_message}")
# -> Output: Outside IF block: Python is awesome!

print("-" * 40)

for temporary_number in range(1, 4):
    pass # Just a placeholder loop

# The loop counter variable still lives even after the loop finished!
print(f"Loop variable after loop ends: {temporary_number}")
# -> Output: Loop variable after loop ends: 3




