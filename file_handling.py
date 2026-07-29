# ==============================================================================
# PYTHON FILE HANDLING 
# ==============================================================================
# File handling allows Python to read, write, append, and delete files.
# File Modes:
# 'r' - Read (Default mode. Opens file for reading, error if missing)
# 'w' - Write (Overwrites existing content or creates a new file)
# 'a' - Append (Adds new data at the end without erasing content)
# 'x' - Create (Creates a new file, returns error if it exists)
# 't' - Text mode (Default)
# 'b' - Binary mode (For images, PDFs, audio)
# ==============================================================================

import os

# ------------------------------------------------------------------------------
# 1. Opening Files & File Paths (Absolute vs Relative)
# ------------------------------------------------------------------------------
# Default open (reads in text mode 'rt' by default)
# Relative Path (looks for file in current directory):
# f = open("demofile.txt")

# Absolute Path (full path specifying exact drive location):
# Note: Double backslashes '\\' are used to escape backslashes in Windows paths
# f = open("D:\\myfiles\\welcome.txt", "r")


# Create a sample file first to use in subsequent examples
f = open("demofile.txt", "w")
f.write("Hello World!\nWelcome to Python File Handling.\nLine 3: Enjoy coding!")
f.close()


# ------------------------------------------------------------------------------
# 2. Classic File Handling Method (Manual open & close)
# ------------------------------------------------------------------------------
# Opening file in read mode
file = open("demofile.txt", "r")

# Read entire content at once
content = file.read()
print("--- Full File Content (Classic Read) ---")
print(content)

# ALWAYS remember to close the file when using classic open()!
file.close()

# Output:
# --- Full File Content (Classic Read) ---
# Hello World!
# Welcome to Python File Handling.
# Line 3: Enjoy coding!


# ------------------------------------------------------------------------------
# 3. Read Only Parts of the File (Characters & Lines)
# ------------------------------------------------------------------------------
# A. Read specific number of characters using read(number)
f = open("demofile.txt", "r")
print("\n--- First 5 Characters Only ---")
print(f.read(5))
f.close()

# Output:
# --- First 5 Characters Only ---
# Hello


# B. Read single line using readline()
f = open("demofile.txt", "r")
print("\n--- Reading Line by Line ---")
print(f.readline().strip())  # Line 1
print(f.readline().strip())  # Line 2
f.close()

# Output:
# --- Reading Line by Line ---
# Hello World!
# Welcome to Python File Handling.


# ------------------------------------------------------------------------------
# 4. Read File by Looping Through Lines (Memory Efficient)
# ------------------------------------------------------------------------------
# By looping through the file object, you can read line-by-line easily
f = open("demofile.txt", "r")
print("\n--- Reading Whole File via Loop ---")
for line in f:
    print(line.strip())
f.close()

# Output:
# --- Reading Whole File via Loop ---
# Hello World!
# Welcome to Python File Handling.
# Line 3: Enjoy coding!


# ------------------------------------------------------------------------------
# 5. Best Practice: Using 'with' Statement & Alias Differences ('f' vs 'file')
# ------------------------------------------------------------------------------
# The 'with' statement automatically closes the file when the block ends.
#
# Difference between 'as f' and 'as file':
# THERE IS NO DIFFERENCE IN FUNCTIONALITY!
# Both 'f' and 'file' are just variable names (aliases) chosen by the programmer.
# 'f' is a short, common convention (like 'i' in loops).
# 'file' is simply a more descriptive variable name.

# Example 1: Using 'as f'
with open("demofile.txt", "r") as f:
    data_f = f.read(12)
    print("\n--- Read using 'as f' ---")
    print(data_f)

# Output:
# --- Read using 'as f' ---
# Hello World!


# Example 2: Using 'as file'
with open("demofile.txt", "r") as file:
    data_file = file.readline().strip()
    print("\n--- Read using 'as file' ---")
    print(data_file)

# Output:
# --- Read using 'as file' ---
# Hello World!


# ------------------------------------------------------------------------------
# 6. Writing ('w') and Appending ('a') Modes
# ------------------------------------------------------------------------------
# Append Mode ('a'): Adds text to the end without deleting existing content
with open("demofile.txt", "a") as f:
    f.write("\nLine 4: This line was appended.")

# Write Mode ('w'): Overwrites the entire file content!
with open("demofile2.txt", "w") as f:
    f.write("Woops! I created a new file or overwritten old content.")


# ------------------------------------------------------------------------------
# 7. Deleting Files and Entire Folders (os module)
# ------------------------------------------------------------------------------
# Check if file exists before deleting to avoid errors
if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
    print("\nFile 'demofile2.txt' deleted successfully.")

# Clean up our primary test file
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("File 'demofile.txt' deleted successfully.")

# Output:
# File 'demofile2.txt' deleted successfully.
# File 'demofile.txt' deleted successfully.


# --- Deleting an Entire Folder ---
# To delete an entire folder, use os.rmdir()
# Note: The folder MUST be empty before calling rmdir(), otherwise Python throws an error.

folder_name = "my_empty_folder"

# Creating folder for demonstration
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Deleting the empty folder
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' removed successfully.")

# Output:
# Folder 'my_empty_folder' removed successfully.