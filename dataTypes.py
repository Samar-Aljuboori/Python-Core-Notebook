# Data Types in Python
#---------------------------------------------------------------------------------------
# 1. Text Type: str
#---------------------------------------------------------------------------------------
user_name = "Samar"
print(f"1. Text Type: {user_name} -> {type(user_name)}")   # Output: <class 'str'>


#---------------------------------------------------------------------------------------
# 2. Numeric Types: int, float, complex
#---------------------------------------------------------------------------------------
age = 29                    # Whole number (int)
height = 162.5              # Decimal number (float)
imaginary_num = 3 + 5j      # Complex number (complex)

print(f"2.1 Integer: {age} -> {type(age)}")
print(f"2.2 Float: {height} -> {type(height)}")
print(f"2.3 Complex: {imaginary_num} -> {type(imaginary_num)}")


#---------------------------------------------------------------------------------------
# 3. Sequence Types: list, tuple, range
#---------------------------------------------------------------------------------------
# List: Ordered, changeable, and allows duplicate members   ---> [ , , ]
skills_list = ["Python", "React", "Figma"]

# Tuple: Ordered, UNCHANGEABLE, and allows duplicate members   ---> ( , , )
coordinates_tuple = (48.81, 9.31)  # e.g., Stuttgart coordinates

# Range: Represents a sequence of numbers (commonly used in loops)   --> range (start, end)
numbers_range = range(1, 6)  # Numbers from 1 to 5

print(f"3.1 List: {skills_list} -> {type(skills_list)}")
print(f"3.2 Tuple: {coordinates_tuple} -> {type(coordinates_tuple)}")
print(f"3.3 Range: {list(numbers_range)} -> {type(numbers_range)}")


#---------------------------------------------------------------------------------------
# 4. Mapping Type: dict
#---------------------------------------------------------------------------------------
# Dictionary: Ordered (since 3.7), changeable, and stores data in Key:Value pairs
developer_profile = {
    "name": "Samar",
    "role": "Full-Stack Developer",
    "experience_years": 3
}
print(f"4. Dictionary: {developer_profile} -> {type(developer_profile)}")


#---------------------------------------------------------------------------------------
# 5. Set Types: set, frozenset
#---------------------------------------------------------------------------------------
# Set: Unordered, UNINDEXED, and NO duplicate members allowed   ---> { , , }
unique_tags = {"python", "ui_ux", "python"}  # Duplicate 'python' will be removed automatically

# Frozenset: Just like a set, but completely immutable (unchangeable)   ---> 
frozen_tags = frozenset({"html", "css"})

print(f"5.1 Set: {unique_tags} -> {type(unique_tags)}")  # Output will only have 2 elements
print(f"5.2 Frozenset: {frozen_tags} -> {type(frozen_tags)}")


#---------------------------------------------------------------------------------------
# 6. Boolean Type: bool
#---------------------------------------------------------------------------------------
# Represents one of two values: True or False
is_backend_developer = True
is_student = False

print(f"6.1 Boolean True: {is_backend_developer} -> {type(is_backend_developer)}")
print(f"6.2 Boolean False: {is_student} -> {type(is_student)}")


#---------------------------------------------------------------------------------------
# 7. Binary Types: bytes, bytearray, memoryview
#---------------------------------------------------------------------------------------
# Used for handling raw binary data (e.g., files, network streams)

byte_data = b"Hello"                 # Bytes (Immutable)
mutable_bytes = bytearray(5)         # Bytearray (Mutable)
mem_view = memoryview(byte_data)     # Allows access to internal buffer data

print(f"7.1 Bytes: {byte_data} -> {type(byte_data)}")
print(f"7.2 Bytearray: {mutable_bytes} -> {type(mutable_bytes)}")
print(f"7.3 Memoryview: {mem_view} -> {type(mem_view)}")


#---------------------------------------------------------------------------------------
# 8. None Type: NoneType
#---------------------------------------------------------------------------------------
# Represents the absence of a value or a null value
database_connection = None
print(f"8. None Type: {database_connection} -> {type(database_connection)}")