# ==============================================================================
# return vs yield
# ==============================================================================
# Concept: 
# - 'return' is for normal functions (returns everything and ends).
# - 'yield' is for generators (returns items one by one on-demand).
# ==============================================================================

# ------------------------------------------------------------------------------
# CASE 1: Using 'return' (The Greed Function)
# ------------------------------------------------------------------------------
def normal_function():
    return "First Item"
    return "Second Item"  # This line is dead code. It will NEVER run!

# Running Fanction
# ------------------------------------------------------------------------------
print("1. Testing 'return':")
result_normal = normal_function()
print(result_normal)  # Output: First Item
# Note: The function died instantly after the first return.

# ------------------------------------------------------------------------------
# CASE 2: Using 'yield' (The Generous Function)
# ------------------------------------------------------------------------------
def generator_function():
    yield "First Item"   # ⏸️ Gives the item, pauses, and waits.
    yield "Second Item"  # ▶️ Wakes up when called again, gives the item, and pauses.

# Running Fanction
# ------------------------------------------------------------------------------
print("\n2. Testing 'yield':")
my_generator = generator_function()

# We get the items ONE BY ONE using next()
print(next(my_generator))  # Output: First Item
print(next(my_generator))  # Output: Second Item
# Note: The function remembered its place and didn't die!