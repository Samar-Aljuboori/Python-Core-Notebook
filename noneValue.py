# None Value in Python
# ---------------------------------------------------------------------------------------------

# 1. This function ONLY prints (Delivery worker with empty hands)
def worker_who_only_prints():
    print("Action: I am screaming in the restaurant!")
    # No return statement here!

# 2. This function RETURNS a value (Delivery worker bringing food)
def worker_who_returns_food():
    return "Delicious Burger "

# ---------------------------------------------------------------------------------------------
# Testing the functions and checking outputs

print("=== CASE 1: Function with Print only ===")
result_1 = worker_who_only_prints()
print(f"What is inside result_1 Box? -> {result_1}")  # What is inside result_1 Box? -> None
# Output will be None because the function didn't return anything.
print("-" * 40)

print("=== CASE 2: Function with Return ===")
result_2 = worker_who_returns_food()
print(f"What is inside result_2 Box? -> {result_2}")
 # What is inside result_2 Box? -> Delicious Burger 
print("-" * 40)

print("=== CASE 3: Checking for None using 'is' ===")
# How to check professionally if a variable is empty (None)
if result_1 is None:
    print("Yes! result_1 is empty (None).")

if result_2 is not None:
    print("Awesome! result_2 has a real value inside it.")