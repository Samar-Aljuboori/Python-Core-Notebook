# 22 Python Exceptions (Error, Description & Example)
#-------------------------------------------------------------------------------------------------

# 1. SyntaxError: Raised when the code violates Python language rules (e.g., missing colon)
try:
    # if x == 5 (Missing colon :)
    pass
except SyntaxError:
    print("SyntaxError caught")

# 2. IndentationError: Raised when spaces or tabs are not aligned correctly
try:
    # def my_func():
    # print("Wrong indentation")
    pass
except IndentationError:
    print("IndentationError caught")

# 3. NameError: Raised when a variable or function name is misspelled or not defined
try:
    print(my_missing_variable)  # type: ignore
except NameError:
    print("NameError caught")

# 4. TypeError: Raised when an operation is applied to an incorrect data type (e.g., string + int)
try:
    result = "Python" + 3
except TypeError:
    print("TypeError caught")

# 5. ValueError: Raised when a function gets a correct type but invalid content (e.g., letters to int)
try:
    number = int("Stuttgart")
except ValueError:
    print("ValueError caught")

# 6. IndexError: Raised when trying to access a list element outside its available range
try:
    my_list = [10, 20]
    print(my_list[5])
except IndexError:
    print("IndexError caught")

# 7. KeyError: Raised when searching for a dictionary key that does not exist
try:
    my_dict = {"name": "Samar"}
    print(my_dict["age"])
except KeyError:
    print("KeyError caught")

# 8. ZeroDivisionError: Raised when dividing a number by zero mathematically
try:
    calc = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError caught")

# 9. AttributeError: Raised when calling a method that doesn't belong to the data type
try:
    num = 5
    num.upper()
except AttributeError:
    print("AttributeError caught")

# 10. FileNotFoundError: Raised when trying to open a file that does not exist on the system
try:
    open("not_found_file.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError caught")

# 11. ModuleNotFoundError: Raised when trying to import a library that is not installed
try:
    import non_existent_library  # type: ignore
except ModuleNotFoundError:
    print("ModuleNotFoundError caught")

# 12. ImportError: Raised when a specific function import fails inside an existing module
try:
    from math import this_function_does_not_exist
except ImportError:
    print("ImportError caught")

# 13. OverflowError: Raised when a math calculation result is too large for the memory capacity
try:
    import math
    print(math.exp(1000))
except OverflowError:
    print("OverflowError caught")

# 14. KeyError (In Sets): Raised when trying to remove an element that does not exist inside a Set
try:
    my_set = {1, 2, 3}
    my_set.remove(10)
except KeyError:
    print("KeyError in set caught")

# 15. UnboundLocalError: Raised when a local variable is used inside a function before it is assigned
try:
    x = 10
    def test():
        # print(x)
        # x = 5
        pass
except UnboundLocalError:
    print("UnboundLocalError caught")

# 16. StopIteration: Raised when next() is called on an Iterator that has no more items left
try:
    my_iter = iter([1])
    next(my_iter)
    next(my_iter)
except StopIteration:
    print("StopIteration caught")

# 17. PermissionError: Raised when trying to open a restricted file without system administration rights
try:
    open("/root/secret.txt", "r")
except PermissionError:
    print("PermissionError caught")

# 18. IsADirectoryError: Raised when trying to open a full folder as if it were a simple text file
try:
    open("../Stuttgart_Project", "r")
except IsADirectoryError:
    print("IsADirectoryError caught")

# 19. NotADirectoryError: Raised when directory-specific operations are applied to a regular file
try:
    import os
    os.listdir("14_common_exceptions.py")
except NotADirectoryError:
    print("NotADirectoryError caught")

# 20. UnicodeDecodeError: Raised when a file cannot be read due to incorrect text encoding formats
try:
    # Opening a file with an unsupported encoding standard
    pass
except UnicodeDecodeError:
    print("UnicodeDecodeError caught")

# 21. KeyboardInterrupt: Raised when the developer manually stops an infinite loop (e.g., pressing Ctrl + C)
try:
    # Infinite loop interrupted by the user from the keyboard
    pass
except KeyboardInterrupt:
    print("KeyboardInterrupt caught")

# 22. MemoryError: Raised when an operation runs completely out of RAM space
try:
    # Creating a massive database object that exceeds RAM limits
    pass
except MemoryError:
    print("MemoryError caught")