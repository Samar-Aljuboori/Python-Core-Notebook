# =================================================================
# Python Functions
# =================================================================


# 1. Basic Function (No inputs, No return)
def greet_user():
    print("Step 1: Welcome to the Functions Lesson!")
    print("-" * 50)

#  Calling Function:
greet_user()   # Step 1: Welcome to the Functions Lesson!

#-------------------------------------------------------------------------------------------------
# 2. Function with Parameters & Arguments
def say_hello(name):
    print(f"Step 2: Hello, {name}! (This function uses a parameter)")
    print("-" * 50)

#  Calling Function:
say_hello('Sara')   # Step 2: Hello, Sara! (This function uses a parameter)

#-------------------------------------------------------------------------------------------------
# 3. Function with Return Value (The important concept!)
def add_numbers(num1, num2):
    # This returns a real value to the code, it doesn't just print it
    return num1 + num2

#  Calling Function:
result = add_numbers(10,20)
print(f"Step 3: The result of addition is: {result}")   # Step 3: The result of addition is: 30

#-------------------------------------------------------------------------------------------------
# 4. Function with Default Argument
def display_location(country="Germany"):
    print(f"Step 4: You are learning Python in {country} !")
    print("-" * 50)

#  Calling Function:
display_location()         # Step 4: You are learning Python in Germany !
display_location(' Iraq ') # Step 4: You are learning Python in  Iraq ! 


#-------------------------------------------------------------------------------------------------
# 5. Advanced: Function with *args (Accepts any number of numbers)
def sum_all_numbers(*numbers):
    return sum(numbers)

#  Calling Function:
sum_numbers = sum_all_numbers(1,2,3,4,5)
print (f"Step 5: Sum of all numbers (*args) is: {sum_numbers}")
# Step 5: Sum of all numbers (*args) is: 15

#-------------------------------------------------------------------------------------------------
# 6. Scope Concept: Global vs Local Variables
global_message = "I am Global (Everyone can see me)"

def check_scope():
    local_message = "I am Local (I only live inside this function)"
    print("Step 6: Scope Check:")
    print(f"-> Variable Inside function: {local_message}")
    print(f"-> Variable Outside function: {global_message}")
    print("-" * 50)

#  Calling Function:
check_scope()
# Step 6: Scope Check:
# Variable Inside function: I am Local (I only live inside this function)
# Variable Outside function: I am Global (Everyone can see me)



# =================================================================
#  Python Functions with Docstrings
# =================================================================

def calculate_area(width, height):
    """
    This function calculates the area of a rectangle.
    
    Parameters:
    width (int/float): The width of the rectangle.
    height (int/float): The height of the rectangle.
    
    Returns:
    int/float: The total area.
    """
    return width * height


def multiply_numbers(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y


# =================================================================
# Running and testing
# =================================================================

# When you hover over 'calculate_area' in VS Code, the Docstring will pop up!
area_result = calculate_area(5, 10)
print(f"Rectangle Area: {area_result}") # Rectangle Area: 50



product_result = multiply_numbers(4, 3)
print(f"Multiplication Result: {product_result}") # Multiplication Result: 12