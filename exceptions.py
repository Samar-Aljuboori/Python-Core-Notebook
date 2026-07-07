# Exception Handling & Error Management In Python ---> (try , except , else , finally)

# --------------------------------------------------------------------------------------
# 1. The Core Try-Except Block (Catching Specific System Errors)
# --------------------------------------------------------------------------------------
# Scenario: Preventing server crash during forbidden mathematical operations.

print("--- 1. Handling ZeroDivisionError ---")
try:
    # The code we want to test/run safely
    server_calculation = 30 / 0  
except ZeroDivisionError:
    # The safety net: executes ONLY if a ZeroDivisionError happens
    print("Safety Triggered: Division by zero detected! Sending custom error message to user.")
# -> Output: Safety Triggered: Division by zero detected! Sending custom error message to user.


# --------------------------------------------------------------------------------------
# 2. Handling Multiple Specific Exceptions & Using Alias ('as e')
# --------------------------------------------------------------------------------------
# Scenario: Catching different errors dynamically and printing the system's official message.

print("\n--- 2. Handling Multiple Specific Errors ---")
try:
    frameworks = ["Django", "React"]
    # Trying to access an index that doesn't exist in memory
    print(frameworks[5]) 
except IndexError as e:
    print(f"Index Error Captured: {e}")
except ValueError as e:
    print(f"Value Error Captured: {e}")
# -> Output: Index Error Captured: list index out of range


# --------------------------------------------------------------------------------------
# 3. The Full Quad-Block Architecture: try, except, else, and finally
# --------------------------------------------------------------------------------------
# Scenario: Simulating a secure Database connection or File stream operations.

print("\n--- 3. Testing the Full Quad-Block (try-except-else-finally) ---")
try:
    print("[STEP 1] Attempting to connect to the production database...")
    # Change 'connection_status = True' to False to simulate an exception!
    connection_status = True 
    if not connection_status:
        raise ConnectionError("Database server is offline.")
except ConnectionError as err:
    print(f"[STEP 2 - FAILURE] Catching Error: {err}")
else:
    # Runs ONLY if the try block succeeds with zero exceptions
    print("[STEP 2 - SUCCESS] Connection established! Fetching user dashboard data...")
finally:
    # Runs GUARANTEED no matter what happens (Success or Failure)
    print("[STEP 3 - CLEANUP] Connection stream safely closed. Resources freed from memory.")
# -> Output:
# [STEP 1] Attempting to connect to the production database...
# [STEP 2 - SUCCESS] Connection established! Fetching user dashboard data...
# [STEP 3 - CLEANUP] Connection stream safely closed. Resources freed from memory.


# --------------------------------------------------------------------------------------
# 4. Forcing/Triggering Errors Manually Using 'raise'
# --------------------------------------------------------------------------------------
# Scenario: Enforcing Business Rules (Business Informatics Concept).
# If a user provides an impossible age, we block them by intentionally throwing an error.

print("\n--- 4. Enforcing Business Rules via 'raise' ---")
def register_new_user(age):
    if age < 0:
        # Intentionally triggering a built-in exception with a custom message
        raise ValueError("Registration Denied: Age cannot be a negative value!")
    return f"User successfully registered with age: {age}"

try:
    # Simulating a user typing an invalid input in a web form
    print(register_new_user(-5))
except ValueError as error_msg:
    print(f"Form Validation Alert: {error_msg}")
# -> Output: Form Validation Alert: Registration Denied: Age cannot be a negative value!

