import os
import pandas as pd

# ==============================================================================
# PANDAS ANALYZING DATAFRAMES
# ==============================================================================
# One of the most used method for getting a quick overview of a DataFrame 
# is the head(), tail(), and info() methods.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Dynamic Path Resolution & Data Loading
# ------------------------------------------------------------------------------
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'data.csv')

df = pd.read_csv(file_path)


# ------------------------------------------------------------------------------
# 2. Viewing the Top Rows with head()
# ------------------------------------------------------------------------------
# The head() method returns the headers and a specified number of rows, 
# starting from the top. Default is 5 rows.

print("=== 1. First 5 Rows using head() ===")
print(df.head())

# Expected Output:
#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    150       148     406.0


# ------------------------------------------------------------------------------
# 3. Viewing the Last Rows with tail()
# ------------------------------------------------------------------------------
# The tail() method returns the headers and a specified number of rows, 
# starting from the bottom. Default is 5 rows.

print("\n=== 2. Last 2 Rows using tail(2) ===")
print(df.tail(2))

# Expected Output:
#    Duration  Pulse  Maxpulse  Calories
# 3        45    109       175     282.4
# 4        45    150       148     406.0


# ------------------------------------------------------------------------------
# 4. Getting Information About the Data with info()
# ------------------------------------------------------------------------------
# The info() method gives you more information about the dataset, such as 
# total rows/columns, data types, and non-null values.

print("\n=== 3. DataFrame Summary using info() ===")
df.info()

# Expected Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   Duration  5 non-null      int64  
#  1   Pulse     5 non-null      int64  
#  2   Maxpulse  5 non-null      int64  
#  3   Calories  5 non-null      float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB


# ==============================================================================
# KEY TAKEAWAYS:
# ------------------------------------------------------------------------------
# - head(n): Quick inspection of the first n rows.
# - tail(n): Quick inspection of the last n rows.
# - info(): Provides structural metadata (data types, memory, missing values).
# ==============================================================================