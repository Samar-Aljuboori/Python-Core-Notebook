#  PYTHON OOP CHEAT SHEET
# ==============================================================================

# 1. OOP Concept & Classes/Objects with "pass" Statement
# ------------------------------------------------------------------------------
# OOP is about grouping data and functions into "Objects".
# A Class is the blueprint; an Object is the actual instance.
# A class cannot be empty, but if you need it empty temporarily, use 'pass':

class EmptyClass:
    pass  # Executable without throwing a SyntaxError


# ------------------------------------------------------------------------------
# 2. Main Class Definition containing all concepts
# ------------------------------------------------------------------------------
class Patient:
    
    hospital_name = "Stuttgart General Hospital"
    total_patients = 0

    # Note: 'self' is just a placeholder , it can be named anything (as long as it's the 1st parameter).
    def __init__(self, name, age, patient_id):
        self.name = name          # Object Property 1 
        self.age = age            # Object Property 2
        self.patient_id = patient_id  # Object Property 3 (Number)
        
        # Increments the global class property counter
        Patient.total_patients += 1

    # IMPORTANT RULE: This method MUST return a String. It CANNOT return an Integer.
    # To return numbers, we must convert them to strings using f-string or str().
    def __str__(self):
        # Using f-string to safely convert age (int) to a string representation
        return (f"Patient Name: {self.name} Age: {self.age}")


    # A class can have multiple methods interacting with its properties:
    def update_age(self, new_age):
        self.age = new_age
        print(f"Age updated to: {new_age}")

    def get_details(self):
        return f"ID: {self.patient_id} | Hospital: {self.hospital_name}"


    # These deal with the class itself, using '@classmethod' and 'cls' parameter.
    @classmethod
    def get_total_patients(cls):
        return f"Total registered patients: {cls.total_patients}"


# ==============================================================================
#  EXECUTION & TESTING 
# ==============================================================================

# Creating Objects 
patient1 = Patient("Sarah", 29, 1001)
patient2 = Patient("Kadhem", 35, 1002)

# --- [A] Testing Object & Class Properties ---
print(patient1.name)            #  Output: Sarah
print(patient2.age)             #  Output: 35
print(patient1.hospital_name)   #  Output: Stuttgart General Hospital


# --- [B] Testing the __str__() Method (The Human Voice) ---
# Without __str__, print(patient1) would print memory address like <__main__.Patient object at 0x...>
# With __str__, it prints our formatted string:
print(patient1)                 #  Output: Patient Name: Sarah (Age: 29)


# --- [C] Testing Multiple Methods Working Together ---
patient1.update_age(30)         #  Output: Age updated to: 30
print(patient1)                 #  Output: Patient Name: Sarah (Age: 30)
print(patient1.get_details())   #  Output: ID: 1001 | Hospital: Stuttgart General Hospital


# --- [D] Topic 8: Modifying & Deleting Properties/Objects ---

# 1. Modifying a property directly:
patient1.name = "Sarah Mahmoud"
print(patient1.name)            #  Output: Sarah Mahmoud

# 2. Deleting an Object Property:
del patient1.patient_id

try:
    # Trying to print patient_id after deletion will raise an AttributeError
    print(patient1.patient_id)
except AttributeError as e:
    print(f"Error caught: {e}") 
    #  Output: Error caught: 'Patient' object has no attribute 'patient_id'

# 3. Deleting the Entire Object:
del patient1

try:
    # Trying to access the object 'patient1' will raise a NameError
    print(patient1)
except NameError as e:
    print(f"Error caught: {e}") 
    #  Output: Error caught: name 'patient1' is not defined


# --- [E] Testing Class Methods ---
# Note: patient2 is still in memory, and the counter is correct.
print(Patient.get_total_patients())  # Output: Total registered patients: 2