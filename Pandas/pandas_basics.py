import pandas as pd

# ==============================================================================
# Pandas Basics 
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Pandas Series (create one columns include : data)
# ------------------------------------------------------------------------------
# Syntax : variable_name = pd.Series(data_list, name="Column_Name")

# Used to create a 1-Dimensional labeled array (a single column).

# 1. Creating a Basic Series with Default Numeric Index

ages = [25, 30, 35]
series_ages = pd.Series(ages, name="Age")  

print("=== 1. Pandas Series (Single Column) ===")
print(series_ages)
# Output:
# 0    25
# 1    30
# 2    35

# 2. Creating a Series with Custom Labels (Custom Index)
# Syntax: pd.Series(data, index=['label1', 'label2', ...])

temperatures = [22, 25, 19]
days = ['Monday', 'Tuesday', 'Wednesday']

series_custom = pd.Series(data=temperatures, index=days, name="Temperature")

print("\n=== 2. Series with Custom Index ===")
print(series_custom)
# Output:
# Monday       22
# Tuesday      25
# Wednesday    19


# 3. Accessing Elements in a Series
# You can retrieve values using the index key/label.

print("\n=== 3. Accessing Data ===")
print("Temperature on Tuesday:", series_custom['Tuesday'])
# Output: 25

# ==============================================================================
# 1. Labels & Creating Custom Labels 
# ==============================================================================
# By default, indices are integers (0, 1, 2). 
# Using the `index` argument lets you create custom labels.

values = [10, 20, 30]
custom_labels = ["a", "b", "c"]

# Creating Series with custom labels
series_with_labels = pd.Series(values, index=custom_labels)

print("=== 1. Series with Custom Labels ===")
print(series_with_labels)
# Accessing an element using its label:
print("Value at label 'b':", series_with_labels["b"])  # Output: 20


# ==============================================================================
# 2. Key/Value Objects as Series 
# ==============================================================================
# When passing a Python Dictionary to pd.Series():
# - Dictionary Keys become the Series Labels (Index).
# - Dictionary Values become the Series Data.

calories = {"Day1": 420, "Day2": 380, "Day3": 390}

# Convert dictionary to Series
series_from_dict = pd.Series(calories)

print("\n=== 2. Series from Dictionary (Key/Value) ===")
print(series_from_dict)
# Output:
# Day1    420
# Day2    380
# Day3    390


# ==============================================================================
# Series:
# ------------------------------------------------------------------------------
# - A Series is a 1-Dimensional array holding data of any type.
# - Indexing: By default, NumPy-style positional indexing (0, 1, 2...) is used.
# - Custom Index: Custom string/numeric labels can be assigned to rows.
# ==============================================================================


# ------------------------------------------------------------------------------
# 2. Pandas DataFrame (create one table include : rows and columns)
# ------------------------------------------------------------------------------
# Syntax :  variable_name = pd.DataFrame(dictionary_data)

# Used to create a 2-Dimensional tabular data structure (rows & columns).
# Keys in the dictionary become column headers; values become column rows.

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Stuttgart', 'Berlin', 'Munich']
}

df = pd.DataFrame(data)

print("\n=== 2. Pandas DataFrame (Full Table) ===")
print(df)
# Output:
#       Name  Age      City
# 0    Alice   25  Stuttgart
# 1      Bob   30    Berlin
# 2  Charlie   35    Munich


# ==============================================================================
# 1. Locate Row using .loc[]
# ==============================================================================
data = {
    'Calories': [420, 380, 390],
    'Duration': [50, 40, 45]
}

df = pd.DataFrame(data)

print("=== Single Row Output ===")
print(df.loc[0])

# Output : === Single Row Output ===
#              Calories    420
#              Duration     50
# Name: 0, dtype: int64

print("\n=== Multiple Rows Output ===")
print(df.loc[[0, 1]])

# Output : === Multiple Rows Output ===
#                   Calories  Duration
#              0       420        50
#              1       380        40


# ==============================================================================
# 2. Named Indexes & 3. Locate Named Indexes
# ==============================================================================
df_named = pd.DataFrame(data, index=["day1", "day2", "day3"])

print("\n=== Named Indexes DataFrame ===")
print(df_named)

# Output : === Named Indexes DataFrame ===
#      Calories  Duration
# day1       420        50
# day2       380        40
# day3       390        45


print("\n=== Locate Row by Label ('day2') ===")
print(df_named.loc["day2"])

# Output : === Locate Row by Label ('day2') ===
# Calories    380
# Duration     40
# Name: day2, dtype: int64

# ==============================================================================
# Summary Pandas DataFrame:
# - loc[0]: Fetches rows by numeric position.
# - index=[...]: Assigns custom text labels to DataFrame rows.
# - loc['label']: Fetches rows using assigned text labels.
# - pd.read_csv(): Loads external datasets into a DataFrame.
# ==============================================================================








