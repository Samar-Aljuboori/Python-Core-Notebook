import os
import pandas as pd

# ==============================================================================
# PANDAS READ JSON
# ==============================================================================



# ------------------------------------------------------------------------------
# 1. Dynamic Path Resolution
# ------------------------------------------------------------------------------
# Resolve relative file path based on current script location
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'data.json')


# ------------------------------------------------------------------------------
# 2. Loading JSON File Into a DataFrame
# ------------------------------------------------------------------------------
# Syntax: pd.read_json('filename.json')
# The read_json() function parses JSON text strings/files into a 2D DataFrame.

df = pd.read_json(file_path)


# ------------------------------------------------------------------------------
# 3. Print the Entire DataFrame
# ------------------------------------------------------------------------------
# Similar to CSV files, use to_string() to output the full dataset clearly.

print("=== 1. Printing JSON DataFrame ===")
print(df.to_string())

# Expected Output:
#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    150       148     406.0


# ------------------------------------------------------------------------------
# 4. JSON Objects as Python Dictionaries
# ------------------------------------------------------------------------------
# If your JSON code is not in a file, but in a Python Dictionary, 
# you can load it directly into a DataFrame using pd.DataFrame().

data = {
  "Duration": {"0": 60, "1": 60, "2": 60},
  "Pulse": {"0": 110, "1": 117, "2": 103},
  "Maxpulse": {"0": 130, "1": 145, "2": 135},
  "Calories": {"0": 409.1, "1": 479.0, "2": 340.0}
}

df_dict = pd.DataFrame(data)

print("\n=== 2. Loading Direct Python Dictionary / JSON Structure ===")
print(df_dict)

# === 2. Loading Direct Python Dictionary / JSON Structure ===
#        Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0


# ==============================================================================
# KEY TAKEAWAYS:
# ------------------------------------------------------------------------------
# - pd.read_json(): Loads external .json files directly into a DataFrame.
# - JSON Data: Shares the same key/value structure as Python Dictionaries.
# - df.to_string(): Ensures complete output representation without truncation.
# ==============================================================================