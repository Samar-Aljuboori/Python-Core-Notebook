# =====================================================================
# PYTHON JSON MODULE 
# =====================================================================
import json

# ---------------------------------------------------------------------
# 1. Parsing JSON (Convert JSON String to Python Dictionary)
# Method used: json.loads() -> "load string"
# ---------------------------------------------------------------------

# This is a string that looks like JSON (Imagine it came from an API)
json_string = '{"name": "Sarah", "age": 22, "is_student": true}'

# Convert it to a Python Dictionary
python_dict = json.loads(json_string)

print("=== 1. JSON String converted to Python Dict ===")
print(python_dict)
print(f"Type: {type(python_dict)}")          # Output: <class 'dict'>
print(f"Accessing Name: {python_dict['name']}") # Output: Sarah
print("-" * 60)


# ---------------------------------------------------------------------
# 2. Converting to JSON (Convert Python Dictionary to JSON String)
# Method used: json.dumps() -> "dump string"
# ---------------------------------------------------------------------

# A regular Python Dictionary
user_profile = {
    "username": "coder_girl",
    "skills": ["Python", "Git", "RegEx"],
    "active": True,
    "score": 95.5
}

# Convert Python Dict to JSON String (indent=4 makes it pretty and readable)
json_output = json.dumps(user_profile, indent=4)

print("=== 2. Python Dict converted to JSON String ===")
print(json_output)
print(f"Type: {type(json_output)}")          # Output: <class 'str'>
print("-" * 60)