# Input and Output In Python (I/O)
#---------------------------------------------------------------------------------------
# 1. Basic Output using print()
#---------------------------------------------------------------------------------------
# The print() function sends data to the standard output device (screen).

print("1.1 Simple string output")      # Output : 1.1 Simple string output
print("1.2 Multiple objects:", "Python", "Full-Stack", 2026)      # Output : 1.2 Multiple objects: Python Full-Stack 2026


#---------------------------------------------------------------------------------------
# 2. Advanced print() Arguments: 'sep' and 'end'
#---------------------------------------------------------------------------------------
# 2.1 'sep' parameter: Changes the character that separates the objects (Default is space)
print("\n2.1 Custom Separator (sep):")      # Output : 2.1 Custom Separator (sep):
print("HTML", "CSS", "JavaScript", sep=" -> ") # Output: HTML -> CSS -> JavaScript

# 2.2 'end' parameter: Changes what gets printed at the end of the line (Default is newline '\n')
print("\n2.2 Custom Line Ending (end):")      # Output : 2.2 Custom Line Ending (end):
print("Building backend code...", end=" ")    # Output : Building backend code... Successfully Done!
print("Successfully Done!")       


#---------------------------------------------------------------------------------------
# 3. Professional String Formatting (f-strings)
#---------------------------------------------------------------------------------------
# Introduced in Python 3.6, f-strings provide a clean and readable way to format strings.

project_name = "Vintage Cafe"
completion_year = 2026

print(f"\n3. f-string: The project '{project_name}' was completed in {completion_year}.")
# Output : 3. f-string: The project 'Vintage Cafe' was completed in 2026.

#---------------------------------------------------------------------------------------
# 4. Basic Input using input() & The String Trap
#---------------------------------------------------------------------------------------
# The input() function alerts the program to stop and wait for the user to type something.
# CRITICAL TRAP: input() ALWAYS returns data as a String (str).

print("\n4.1 Receiving Input (Interactive Section):")   
 # Output : 4.1 Receiving Input (Interactive Section):
user_name = input(" -> Enter your name: ")    #  -> Enter your name: samar
print(f"Welcome to Python, Coach {user_name}!")      # Output : Welcome to Python, Coach samar!


#---------------------------------------------------------------------------------------
# 5. Input Type Conversion (Type Casting)
#---------------------------------------------------------------------------------------
# To do mathematical calculations, you must wrap input() inside int() or float().

print("\n5.1 Numeric Input Conversion:")      # Output :5.1 Numeric Input Conversion: 
birth_year = int(input(" -> Enter your birth year (e.g., 1997): "))      
# Output :  -> Enter your birth year (e.g., 1997): 1996

# Calculation works safely because birth_year is converted to an Integer
current_year = 2026
calculated_age = current_year - birth_year
print(f"Calculated Age in {current_year}: {calculated_age} years old.")      
# Output : Calculated Age in 2026: 30 years old.

# Float handling example
print("\n5.2 Float Input Conversion:")      # Output : 5.2 Float Input Conversion:
item_price = float(input(" -> Enter product price in Euro (€): "))
#  -> Enter product price in Euro (€): 10.99
discounted_price = item_price * 0.90          # 10% off
print(f"Price after 10% discount: {discounted_price:.2f} €")
# Output : Price after 10% discount: 9.89 €