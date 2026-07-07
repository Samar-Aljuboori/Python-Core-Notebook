# ------------------------------------------------------------------------------
# Python Iterators: Understanding Behind-the-Scenes Loops
# ------------------------------------------------------------------------------

print("--- DEMONSTRATING PYTHON ITERATORS ---")

# 1. Creating a normal Iterable (A Python List)
my_fruits = ["Apple", "Banana", "Cherry"]

# 2. Transforming the List into an Iterator object using iter()
fruit_iterator = iter(my_fruits)

print(f"Iterator Object Type: {type(fruit_iterator)}")
# -> Output: Iterator Object Type: <class 'list_iterator'>


# 3. Pulling items manually using next()
print("\nFetching items manually:")

print(next(fruit_iterator)) # -> Output: Apple
print(next(fruit_iterator)) # -> Output: Banana
print(next(fruit_iterator)) # -> Output: Cherry

# 4. CRITICAL RULE: What happens if we call next() again?
# There are no more items left! It will raise a StopIteration.
print("\nCalling next() one more time triggers StopIteration:")

try:
    print(next(fruit_iterator))
except StopIteration:
    print("Result: StopIteration caught! The Iterator is completely empty.")
    # -> Output: Result: StopIteration caught! The Iterator is completely empty.



#---------------------------------------------------------------------------------------------
# Example : Creating a question pool for a Quiz Application
#----------------------------------------------------------------------------------------------
questions = ["What is Python?", "What is a Loop?", "What is an Array?"]

# Converting the list into an Iterator object for manual control
quiz_dealer = iter(questions)

print("--- QUIZ APPLICATION SIMULATION ---")

# Step 1: The UI loads and triggers only the first question
print(next(quiz_dealer)) 
# -> Output: What is Python?

# ------------------------------------------------------------------------------
# [NOTE] Here, a long block of code would execute to process the user's answer,
# validate their input, and wait for them to click the "Next" button.
# ------------------------------------------------------------------------------

# Step 2: The user clicks the "Next" button, triggering the second question
print(next(quiz_dealer)) 
# -> Output: What is a Loop?

# Step 3: The user clicks "Next" again, triggering the third question
print(next(quiz_dealer)) 
# -> Output: What is an Array?