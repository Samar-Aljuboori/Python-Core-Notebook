# =================================================================
#  *args and **kwargs in Python
# =================================================================

# 1. Understanding *args (Collects elements into a Tuple)
def multiply_all(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

# Calling Fanction:
print("=== Case 1: Testing *args ===")
# You can pass 3 numbers or 5 numbers seamlessly
print(f"Multiplying 2, 3, 4: {multiply_all(2, 3, 4)}")           # Multiplying 2, 3, 4: 24
print(f"Multiplying 1, 5, 10, 2: {multiply_all(1, 5, 10, 2)}")   # Multiplying 1, 5, 10, 2: 100


# =================================================================
# 2. Understanding **kwargs (Collects elements into a Dictionary)
def show_user_profile(username, **additional_info):
    print(f"User: {username}")
    if additional_info:
        print("Additional Details:")
        for key, value in additional_info.items():
            print(f"- {key}: {value}")

# Calling Fanction:
print("=== Case 2: Testing **kwargs ===")
# Scenario A: Only passing the required username
show_user_profile("mona_dev")

# Scenario B: Passing extra details using keywords
show_user_profile("ali_engineer", role="Admin", location="Iraq", experience="5 years")
#  User: mona_dev
#  User: ali_engineer
#  Additional Details:
#- role: Admin
#- location: Iraq
#- experience: 5 years








#git commit -m "Add focused guide on Python args and kwargs feature"