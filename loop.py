# Python Loops (for, while, break, continue, pass)
#---------------------------------------------------------------------------------------
# 1. The Basic 'for' Loop (Iterating over Sequences)
#---------------------------------------------------------------------------------------
# A 'for' loop is used for iterating over a sequence (list, tuple, dictionary, set, or string).

tech_stack = ["Python", "Django", "React"]

print("1. Iterating over a list:")
for framework in tech_stack:
    print(framework)
# OUTPUT:
# Python
# Django
# React


#---------------------------------------------------------------------------------------
# 2. Loop Through a String
#---------------------------------------------------------------------------------------
# Even strings are iterable objects, they contain a sequence of characters.

word = "Python"

print("\n2. Iterating over a string:")
for letter in word:
    print(letter)
# OUTPUT:
# P
# y
# t
# h
# o
# n


#---------------------------------------------------------------------------------------
# 3. The range() Function (Controlling Loop Iterations)
#---------------------------------------------------------------------------------------
# To loop through a set of code a specified number of times, we use range().
# range(start, stop, step) -> Note that it stops at stop-1.

print("\n3.1 Using range(stop):")
for i in range(3):
    print(i)       # OUTPUT: 0, 1, 2 (Starts from 0 by default)

print("\n3.2 Using range(start, stop):")
for i in range(5, 8):
    print(i)      # OUTPUT: 5, 6, 7

print("\n3.3 Using range(start, stop, step):")
for i in range(1, 10, 2):
    print(i)      # OUTPUT: 1, 3, 5, 7, 9 (Increments by 2)


#---------------------------------------------------------------------------------------
# 4. The Basic 'while' Loop (Condition-Based Iteration)
#---------------------------------------------------------------------------------------
# A 'while' loop executes a set of statements as long as a condition is True.
# CRITICAL: Always remember to increment the iterator, otherwise it loops forever!

counter = 1

print("\n4. Executing while loop:")
while counter <= 3:
    print(f"Count: {counter}")
    counter += 1
# OUTPUT:
# Count: 1
# Count: 2
# Count: 3


#---------------------------------------------------------------------------------------
# 5. The 'break' Statement (Exiting the Loop Prematurely)
#---------------------------------------------------------------------------------------
# Used to stop/exit the loop immediately, even if the loop condition or sequence is not finished.

print("\n5.1 Testing 'break' in a for loop:")
for num in range(1, 10):
    if num == 4:
        break # Stops the loop when num reaches 4
    print(num)
# OUTPUT: 1, 2, 3

print("\n5.2 Testing 'break' in a while loop:")
x = 5
while x > 0:
    if x == 3:
        break
    print(x)
    x -= 1
# OUTPUT: 5, 4


#---------------------------------------------------------------------------------------
# 6. The 'continue' Statement (Skipping the Current Iteration)
#---------------------------------------------------------------------------------------
# Stops the current iteration of the loop, and continues/jumps to the next iteration.

print("\n6.1 Testing 'continue' in a for loop:")
for num in range(1, 5):
    if num == 3:
        continue # Skips printing 3
    print(num)
# OUTPUT: 1, 2, 4

print("\n6.2 Testing 'continue' in a while loop:")
y = 0
while y < 4:
    y += 1
    if y == 2:
        continue # Skips the rest of code when y is 2
    print(y)
# OUTPUT: 1, 3, 4


#---------------------------------------------------------------------------------------
# 7. The 'else' Block in Loops (Python Unique Feature)
#---------------------------------------------------------------------------------------
# The 'else' block runs ONLY when the loop completes naturally without hitting a 'break'.

print("\n7.1 Else block executed (Loop finished successfully):")
for n in range(3):
    print(n)
else:
    print("Loop finished naturally!") 
# OUTPUT:
# 0
# 1
# 2
# Loop finished naturally!

print("\n7.2 Else block SKIPPED (Loop interrupted by break):")
for n in range(3):
    if n == 1:
        break
    print(n)
else:
    print("This will NOT be printed.")
# OUTPUT: 0


#---------------------------------------------------------------------------------------
# 8. Nested Loops (Loop inside a Loop)
#---------------------------------------------------------------------------------------
# The "inner loop" will be executed one whole time for each iteration of the "outer loop".

adj = ["Big", "Tasty"]
fruits = ["Apple", "Banana"]

print("\n8. Nested Loops Execution:")
for x in adj:
    for y in fruits:
        print(x, y)
# OUTPUT:
# Big Apple
# Big Banana
# Tasty Apple
# Tasty Banana


#---------------------------------------------------------------------------------------
# 9. The 'pass' Statement Placeholder
#---------------------------------------------------------------------------------------
# Loops cannot be empty. Put 'pass' to avoid syntax errors if you plan to write code later.

print("\n9. Pass loop executed:")
for x in [0, 1, 2]:
    pass # Code placeholder. Python bypasses smoothly.
print("Loop passed successfully without errors.")
# OUTPUT: Loop passed successfully without errors.