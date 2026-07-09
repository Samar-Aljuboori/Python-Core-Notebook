import re

def run_regex_examples():
    # ---------------------------------------------------------
    # Example 1: Finding Phone Numbers using \d (Digits)
    # ---------------------------------------------------------
    text_1 = "Call me at 123-456-7890 , office number 987-654-3210 or 8764-432-7643 ."
    
    # Pattern meaning: 3 digits, then a dash, 3 digits, dash, 4 digits
    phone_pattern = r"\b\d{3}-\d{3}-\d{4}"
    
    # findall gets ALL phone numbers in a list
    all_phones = re.findall(phone_pattern, text_1)
    
    print("=== Example 1: Extracted Phone Numbers ===")
    print(all_phones) 
    print("-" * 50)

    # ---------------------------------------------------------
    # Example 2: Finding Email Addresses
    # ---------------------------------------------------------
    text_2 = "Contact us at support@example.com or hr@company.de today."
    
    # Pattern to match basic email structures
    email_pattern = r"[\w.-]+@[\w.-]+\.\w+"
    
    all_emails = re.findall(email_pattern, text_2)
    
    print("=== Example 2: Extracted Emails ===")
    print(all_emails)
    print("-" * 50)

    # ---------------------------------------------------------
    # Example 3: Replacing text using re.sub
    # ---------------------------------------------------------
    text_3 = "The secret code is SECRET123 and another is SECRET999"
    
    # Hide any digits after the word SECRET
    hidden_text = re.sub(r"SECRET\d+", "[HIDDEN]", text_3)
    
    print("=== Example 3: Hiding Sensitive Data ===")
    print(hidden_text)
    print("-" * 50)

# Run the function directly
run_regex_examples()




text = "Hello 123 !_"

# \d -> will find: ['1', '2', '3']
# \D -> will find: ['H', 'e', 'l', 'l', 'o', ' ', ' ', '!', '_']

# \w -> will find: ['H', 'e', 'l', 'l', 'o', '1', '2', '3', '_']
# \W -> will find: [' ', ' ', '!']

# \s -> will find the two spaces: [' ', ' ']
# \S -> will find all visible characters: ['H', 'e', 'l', 'l', 'o', '1', '2', '3', '!', '_']





# =====================================================================
# SUMMARY TABLE FOR REGEX CHARACTERS (SMALL VS CAPITAL)
# =====================================================================
#
#  SYMBOL (Small)  |  WHAT IT MATCHES            |  SYMBOL (Capital) |  WHAT IT MATCHES
# -----------------|-----------------------------|-------------------|-----------------------------
#  \d (Digit)      |  Any NUMBER (0-9)           |  \D (Non-Digit)   |  Anything EXCEPT numbers
#  \w (Word)       |  Letters, Numbers, and _    |  \W (Non-Word)    |  Symbols, Spaces, Punctuation
#  \s (Space)      |  Only White Spaces / Tabs   |  \S (Non-Space)   |  Anything EXCEPT spaces
#
# =====================================================================

# 💡 QUICK REMINDER:
# The lowercase letter does the action, and the UPPERCASE letter does the EXACT opposite!