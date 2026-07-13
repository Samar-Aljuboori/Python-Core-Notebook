# ==============================================================================
# Python Decorators (Function Filters) 
# Description: A reusable template to add features before and after functions.
# ==============================================================================

# 1. This is the Standard Template (The Filter)
def my_filter(original_function):
    def wrapper():
        # WRITE WHAT YOU WANT TO HAPPEN BEFORE HERE:
        print("[BEFORE] >>> Doing something before the main function runs...")
        
        # This executes your main function
        original_function()
        
        # WRITE WHAT YOU WANT TO HAPPEN AFTER HERE:
        print("[AFTER] >>> Doing something after the main function ends...\n")
        
    return wrapper


# 2. How to use it on your functions using @
@my_filter
def say_hello():
    print("Main Function: Hello Samar!")

@my_filter
def say_goodbye():
    print("Main Function: Goodbye!")


# 3. Testing the functions
say_hello()
say_goodbye()