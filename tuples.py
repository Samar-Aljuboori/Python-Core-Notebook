#Tuple in Python
#-------------------------------------------
# 1. Creating a Tuple
#--------------------
coordinates = (48.7758, 9.1829)
hobbies = ("Walking", "Cooking", "Reading", "Walking") # Allows duplicates

print(f"Coordinates Tuple: {coordinates}")              # Output:Coordinates Tuple: (48.7758, 9.1829)
print(f"Hobbies Tuple: {hobbies}\n")                    # Output:Hobbies Tuple: ('Walking', 'Cooking', 'Reading', 'Walking')

# 2. Accessing Items (Same as Lists using Index)
#-----------------------------------------------
print(f"First Hobby: {hobbies[0]}")  # Output: Walking
print(f"Last Hobby: {hobbies[-1]}")   # Output: Walking

# 3. Tuple Methods (Only 2 methods exist because it's immutable!)
#----------------------------------------------------------------
# Counts how many times an item appears   ---> count() 
print(f"How many times 'Walking' appears: {hobbies.count('Walking')}") # Output: 2

# Finds the first position of an item    ---> index()
print(f"Index of 'Cooking': {hobbies.index('Cooking')}") # Output: 1

# 4. Critical Note: Immutability
#--------------------------------
# If you try to run the line below, Python will throw a TypeError:
# hobbies[0] = "Crochet"  # ❌ NOT ALLOWED!

# 5. Trick: Creating a Tuple with ONLY ONE item
# You MUST include a trailing comma, otherwise Python thinks it's a regular string/integer
wrong_tuple = ("Python")            # Type: str
correct_tuple = ("Python",)         # Type: tuple
print(f"\nType of correct_tuple: {type(correct_tuple)}")        #Output: Type of correct_tuple: <class 'tuple'>




# 6. Unpacking
#---------------
# Having a tuple with 3 items
user_data = ("Samar", 29, "Germany")

# Unpacking it into 3 separate variables
name, age, country = user_data

print(name)     # Output: Samar
print(age)      # Output: 29
print(country)  # Output: Germany


# 7. *Asterisk
#--------------
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Using asterisk to collect the remaining items
first, second, *remaining = fruits

print(first)      # Output: apple
print(second)     # Output: banana
print(remaining)  # Output: ['cherry', 'date', 'elderberry'] (Notice it becomes a List!)




# 8. Tuples (Join & Multiply)
#---------------------------
tuple1 = ("a", "b")
tuple2 = (1, 2)

# Join 
#-------
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: ('a', 'b', 1, 2)

# Multiply 
#---------
multiplied_tuple = tuple1 * 3
print(multiplied_tuple)  # Output: ('a', 'b', 'a', 'b', 'a', 'b')


# 9. Python Tuple Length ---->  len() 
#-------------------------------------
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total Items:', len(cars))       # Output: Total Items: 4


# Check if an Item Exists in the Tuple  ---> (in) Keyword
# -------------------------------------
colors = ('red', 'orange', 'blue')

print('yellow' in colors)    # False
print('red' in colors)       # True 



# 10. Delete Tuple     ---> (del) Keyword
#-----------------
animals = ('dog', 'cat', 'rat')
del animals  



