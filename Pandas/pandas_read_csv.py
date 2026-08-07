import os
import pandas as pd

# ==============================================================================
# PANDAS READ CSV 
# ==============================================================================
# A simple way to store big datasets is to use CSV files (Comma Separated Files).
# CSV files contain plain text and are a well-known format that can be read 
# by everyone, including Pandas.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Dynamic Path Resolution (Handling File Locations)
# ------------------------------------------------------------------------------
# In real-world projects, executing scripts from different terminal working 
# directories can cause "FileNotFoundError". 
# Using `os.path.dirname(__file__)` ensures Python locates the CSV file relative 
# to the script's actual directory.

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'data.csv')


# ------------------------------------------------------------------------------
# 2. Loading CSV Into a DataFrame
# ------------------------------------------------------------------------------
# Syntax: pd.read_csv('filename.csv')
# The read_csv() function loads the comma-separated data into a 2D DataFrame.

df = pd.read_csv(file_path)


# ------------------------------------------------------------------------------
# 3. Print the Entire DataFrame (to_string)
# ------------------------------------------------------------------------------
# If you have a large DataFrame, Pandas will only print the first 5 rows and 
# the last 5 rows by default.
# Use to_string() to print the entire DataFrame.

print("=== 1. Printing Full DataFrame ===")
print(df.to_string())

# Expected Output:
#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    150       148     406.0


# ------------------------------------------------------------------------------
# 4. Understanding max_rows Configuration
# ------------------------------------------------------------------------------
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with `pd.options.display.max_rows`.
# By default, most environments limit this to 60 rows.

print("\n=== 2. Checking System Default Max Rows ===")
print(pd.options.display.max_rows)

# Expected Output:
# 60


# ------------------------------------------------------------------------------
# 5. Modifying max_rows Limit
# ------------------------------------------------------------------------------
# If the DataFrame has more rows than the max_rows limit, printing it without 
# .to_string() will show only the headers and the top/bottom 5 rows (truncated).
# You can change the maximum rows number to display the entire dataset:

pd.options.display.max_rows = 9999

print("\n=== 3. Printing DataFrame After Increasing Max Rows ===")
print(df)


# ==============================================================================
# KEY TAKEAWAYS:
# ------------------------------------------------------------------------------
# - pd.read_csv(): Reads tabular data from external CSV files.
# - df.to_string(): Converts the full DataFrame into a clean string representation.
# - pd.options.display.max_rows: Global system parameter governing printed rows.
# ==============================================================================