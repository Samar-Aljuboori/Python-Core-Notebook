# =================================================================
# Python Function Arguments
# =================================================================

# 1. Positional & Keyword Arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Calling Function:
print("=== 1. Positional vs Keyword ===")
display_info("Mona", 22)                # Name: Mona, Age: 22
display_info(age=25, name="Ali")         # Name: Ali, Age: 25

# =================================================================

# 2. Default Arguments
def power_of(number, exponent=2):
    return number ** exponent

# Calling Function:
print("=== 2. Default Values ===")
print(f"Square of 5: {power_of(5)}")    # Square of 5: 25
print(f"Cube of 2: {power_of(2, 3)}")   # Cube of 2: 8

# =================================================================

# 3. Variable-length Arguments (*args)
def calculate_average(*scores):
 return sum(scores) / len(scores)

# Calling Function:
print("=== 3. Using *args ===")
avg = calculate_average(85, 90, 75, 100)
print(f"The average score is: {avg}")   # The average score is: 87.5
# =================================================================

# 4. Keyword Variable-length Arguments (**kwargs --> KeyWord Arguments)  
def print_scores_report(student_name, **subjects):
    print(f"=== Report Card for {student_name} ===")
    for subject, score in subjects.items():
        print(f"{subject}: {score}")

# Calling Function:
print("=== 4. Using **kwargs ===")
print_scores_report("Sarah", Math=95, Science=88, History=92)


