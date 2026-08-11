import os
import numpy as np
import pandas as pd

# ==============================================================================
# PANDAS DATA CLEANING 
# ==============================================================================


# ==============================================================================
# 1. MISSING DATA FUNCTIONS OVERVIEW
# ==============================================================================
# 1. np.nan:
#    - Represents 'Not a Number' (missing/null values) in pandas and numpy.
#    - Used as a placeholder for unknown or unrecorded values in dataframes.
#
# 2. isnull().sum():
#    - isnull(): Returns a boolean mask (True for NaN, False for valid data).
#    - .sum(): Counts total missing (True) values per column for evaluation.
#
# 3. fillna():
#    - Imputes/fills NaN slots with a designated constant or metric (e.g., mean/median/mode).
#    - Keeps sample size intact without dropping entire rows.
#
# 4. dropna():
#    - Removes rows or columns containing missing (NaN) values entirely.
#    - Ideal when missing entries cannot be inferred or are irrelevant.
# ==============================================================================

raw_missing_data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva'],
    'Age': [25, np.nan, 30, 22, 35],
    'Salary': [50000, 60000, 55000, np.nan, 70000],
    'Department': ['HR', 'IT', 'IT', np.nan, 'HR'],
}

df_missing = pd.DataFrame(raw_missing_data)

print("=== 1. Check Missing Values Count ===")
print(df_missing.isnull().sum())

# Expected Output:
# Employee_ID    0
# Name           1
# Age            1
# Salary         1
# Department     1
# dtype: int64

# Impute missing values using statistical metrics and placeholders
df_missing['Age'] = df_missing['Age'].fillna(df_missing['Age'].median())
df_missing['Salary'] = df_missing['Salary'].fillna(df_missing['Salary'].mean())
df_missing['Department'] = df_missing['Department'].fillna(
    df_missing['Department'].mode()[0]
)
df_missing['Name'] = df_missing['Name'].fillna('Unknown')

print("\n=== 2. DataFrame After Missing Data Imputation ===")
print(df_missing.to_string())

# Expected Output:
#    Employee_ID     Name   Age   Salary Department
# 0          101    Alice  25.0  50000.0         HR
# 1          102      Bob  27.5  60000.0         IT
# 2          103  Unknown  30.0  55000.0         IT
# 3          104    David  22.0  58750.0         HR
# 4          105      Eva  35.0  70000.0         HR


# ------------------------------------------------------------------------------
# 2. Removing Duplicate Records
# ------------------------------------------------------------------------------
# Duplicate records corrupt analyses. Use duplicated().sum() and drop_duplicates().

raw_duplicate_data = {
    'Transaction_ID': [1, 2, 2, 3, 4, 1],
    'Customer': ['Samar', 'Mahmoud', 'Mahmoud', 'Sarah', 'Ali', 'Samar'],
    'Amount': [100, 250, 250, 300, 150, 100],
}

df_duplicates = pd.DataFrame(raw_duplicate_data)

print("\n=== 3. Count Total Duplicate Rows ===")
print(df_duplicates.duplicated().sum())

# Expected Output:
# 2

df_unique = df_duplicates.drop_duplicates()

print("\n=== 4. DataFrame After Deduplication ===")
print(df_unique.to_string())

# Expected Output:
#    Transaction_ID Customer  Amount
# 0               1    Samar     100
# 1               2  Mahmoud     250
# 3               3    Sarah     300
# 4               4      Ali     150


# ------------------------------------------------------------------------------
# 3. Fixing Data Types & Format Parsing
# ------------------------------------------------------------------------------
# Import processes often load numbers or dates as plain text (objects).
# Use astype(), pd.to_numeric(), and pd.to_datetime() to resolve data types.

raw_type_data = {
    'Item_ID': ['1', '2', '3', '4'],
    'Price': ['$10.50', '$20.00', 'FREE', '$15.75'],
    'Date': ['2026-01-15', '2026/02/20', 'Invalid_Date', '2026-03-05'],
}

df_types = pd.DataFrame(raw_type_data)

print("\n=== 5. Data Types Before Conversion ===")
print(df_types.dtypes)

# Expected Output:
# Item_ID    object
# Price      object
# Date       object
# dtype: object

# Conversion step
df_types['Item_ID'] = df_types['Item_ID'].astype(int)
df_types['Price'] = df_types['Price'].str.replace('$', '', regex=False)
df_types['Price'] = pd.to_numeric(df_types['Price'], errors='coerce')
df_types['Date'] = pd.to_datetime(df_types['Date'], errors='coerce')

print("\n=== 6. Processed DataFrame with Correct Data Types ===")
print(df_types.to_string())

# Expected Output:
#    Item_ID  Price       Date
# 0        1  10.50 2026-01-15
# 1        2  20.00 2026-02-20
# 2        3    NaN        NaT
# 3        4  15.75 2026-03-05

print("\n=== 7. Data Types After Conversion ===")
print(df_types.dtypes)

# Expected Output:
# Item_ID             int64
# Price             float64
# Date       datetime64[ns]
# dtype: object


# ------------------------------------------------------------------------------
# 4. Text & String Cleaning
# ------------------------------------------------------------------------------
# Clean strings by removing leading/trailing spaces and non-digit characters.

raw_text_data = {
    'City': ['  stuttgart ', 'BERLIN  ', 'munich', '  FRANKFURT '],
    'Phone': ['123-456-789', '(987) 654-3210', '555.444.3333', '111 222 333'],
}

df_text = pd.DataFrame(raw_text_data)

# Normalize text casing and strip whitespace
df_text['City'] = df_text['City'].str.strip().str.title()

# Remove non-digit regex patterns from phone column
df_text['Phone'] = df_text['Phone'].str.replace(r'\D', '', regex=True)

print("\n=== 8. Cleaned Text and String Columns ===")
print(df_text.to_string())

# Expected Output:
#         City        Phone
# 0  Stuttgart   123456789
# 1     Berlin  9876543210
# 2     Munich  5554443333
# 3  Frankfurt   111222333


# ------------------------------------------------------------------------------
# 5. Handling Invalid Values & Outliers
# ------------------------------------------------------------------------------
# Fix logic bugs (negative ages) and limit extreme scores using clip() or filtering.

raw_outlier_data = {
    'User': ['A', 'B', 'C', 'D'],
    'Age': [25, -3, 150, 30],
    'Score': [85, 92, 78, 1050],  # Maximum valid score is 100
}

df_outliers = pd.DataFrame(raw_outlier_data)

# Fix sign error
df_outliers['Age'] = df_outliers['Age'].abs()

# Filter out unrealistic ages
df_outliers = df_outliers[df_outliers['Age'] <= 120]

# Cap scores to upper limit of 100
df_outliers['Score'] = df_outliers['Score'].clip(upper=100)

print("\n=== 9. DataFrame After Handling Outliers and Logic Errors ===")
print(df_outliers.to_string())

# Expected Output:
#   User  Age  Score
# 0    A   25     85
# 1    B    3     92
# 3    D   30    100


# ------------------------------------------------------------------------------
# 6. Standardizing Column Names
# ------------------------------------------------------------------------------
# Clean headers by removing spaces, lowercasing, and turning hyphens into underscores.

raw_columns_data = {
    ' Customer Name ': ['Alice', 'Bob'],
    'ORDER-DATE': ['2026-01-01', '2026-01-02'],
    'Total Amount ($)': [100, 200],
}

df_cols = pd.DataFrame(raw_columns_data)

print("\n=== 10. Original Column Headers ===")
print(list(df_cols.columns))

# Expected Output:
# [' Customer Name ', 'ORDER-DATE', 'Total Amount ($)']

df_cols.columns = (
    df_cols.columns.str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('-', '_')
    .str.replace(r'[^\w\s]', '', regex=True)
)

print("\n=== 11. Cleaned Column Headers ===")
print(list(df_cols.columns))

# Expected Output:
# ['customer_name', 'order_date', 'total_amount_']


# ------------------------------------------------------------------------------
# 7. Complete End-to-End Cleaning Pipeline
# ------------------------------------------------------------------------------
# Combining all cleaning techniques into a cohesive data transformation script.

raw_pipeline_data = {
    ' Cust ID ': [101, 102, 102, 103, 104],
    'Name': [
        '  john doe ',
        'SARAH SMITH ',
        'SARAH SMITH ',
        'michael brown ',
        '  eva green ',
    ],
    'Age': [28, -34, -34, np.nan, 22],
    'Salary': ['$4,500', '$5,200', '$5,200', 'INVALID', '$3,900'],
    'Join Date': [
        '2026-01-10',
        '2026/02/15',
        '2026/02/15',
        '2026-03-01',
        'Bad_Date',
    ],
}

df_pipeline = pd.DataFrame(raw_pipeline_data)

print("\n=== 12. Raw Uncleaned Pipeline Dataset ===")
print(df_pipeline.to_string())

# Expected Output:
#     Cust ID            Name   Age   Salary   Join Date
# 0       101      john doe    28.0   $4,500  2026-01-10
# 1       102    SARAH SMITH  -34.0   $5,200  2026/02/15
# 2       102    SARAH SMITH  -34.0   $5,200  2026/02/15
# 3       103  michael brown    NaN  INVALID  2026-03-01
# 4       104     eva green    22.0   $3,900    Bad_Date

# Pipeline execution steps:
df_pipeline.columns = (
    df_pipeline.columns.str.strip().str.lower().str.replace(' ', '_')
)
df_pipeline = df_pipeline.drop_duplicates()
df_pipeline['name'] = df_pipeline['name'].str.strip().str.title()
df_pipeline['age'] = df_pipeline['age'].abs()
df_pipeline['age'] = df_pipeline['age'].fillna(df_pipeline['age'].median())
df_pipeline['salary'] = (
    df_pipeline['salary']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
)
df_pipeline['salary'] = pd.to_numeric(df_pipeline['salary'], errors='coerce')
df_pipeline['salary'] = df_pipeline['salary'].fillna(
    df_pipeline['salary'].mean()
)
df_pipeline['join_date'] = pd.to_datetime(
    df_pipeline['join_date'], errors='coerce'
)

print("\n=== 13. Final Cleaned Pipeline Dataset ===")
print(df_pipeline.to_string())

# Expected Output:
#    cust_id           name   age  salary  join_date
# 0      101       John Doe  28.0  4500.0 2026-01-10
# 1      102    Sarah Smith  34.0  5200.0 2026-02-15
# 3      103  Michael Brown  28.0  4533.3 2026-03-01
# 4      104      Eva Green  22.0  3900.0        NaT


# ==============================================================================
# KEY TAKEAWAYS:
# ------------------------------------------------------------------------------
# - isnull().sum() & fillna(): Crucial for detecting and imputing missing data.
# - drop_duplicates(): Essential for maintaining unique entity records.
# - to_numeric() & to_datetime(): Handle invalid string parsing gracefully.
# - str methods: Normalize text casing and remove excess symbols/whitespaces.
# ==============================================================================