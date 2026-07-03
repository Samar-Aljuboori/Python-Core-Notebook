# Matching  In Python (match...case)
#---------------------------------------------------------------------------------------
# 1. Basic match...case Structure
#---------------------------------------------------------------------------------------
# Replaces complex if-elif-else chains with cleaner, more readable pattern matching.

user_role = "editor"

print("1. Testing Basic Match Case:")       # Output : 1. Testing Basic Match Case:
match user_role:
    case "admin":
        print(" - Action: Redirect to Full Admin Control Panel.")
    case "editor":
        print(" - Action: Open Content Management System.") # Executed
    case "guest":
        print(" - Action: Display Read-Only Dashboard.")
    case _:
        print(" - Action: Access Denied. Unknown Role.") # The default fallback (else)
# Output :  - Action: Open Content Management System.

#---------------------------------------------------------------------------------------
# 2. Matching Multiple Patterns using the Pipe Operator (|)
#---------------------------------------------------------------------------------------
# You can combine multiple cases into a single line using '|' which acts as a logical OR.

http_status = 404

print("\n2. Testing Combined Patterns (|):")      # Output :2. Testing Combined Patterns (|):
match http_status:
    case 200 | 201 | 204:
        print(" - Server Response: Request Succeeded.")
    case 400 | 401 | 404:
        print(" - Server Response: Client-Side Error Detected.") # Executed
    case 500 | 503:
        print(" - Server Response: Critical Infrastructure Error.")
    case _:
        print(" - Server Response: Undefined Status Code.")
# Output :  - Server Response: Client-Side Error Detected.

#---------------------------------------------------------------------------------------
# 3. Pattern Matching with Conditions (Guards)
#---------------------------------------------------------------------------------------
# You can add an 'if' statement inside a case block. This is called a "Guard".

age = 29

print("\n3. Testing Match Case with Guards:")     # Output : 3. Testing Match Case with Guards:
match age:
    case int() if age < 13:
        print(" - Profile Category: Child Account.")
    case int() if age >= 13 and age < 20:
        print(" - Profile Category: Teenager Account.")
    case int() if age >= 20:
        print(" - Profile Category: Adult Professional Account.") # Executed
    case _:
        print(" - Profile Category: Invalid Age Type.")
# Output :  - Profile Category: Adult Professional Account.