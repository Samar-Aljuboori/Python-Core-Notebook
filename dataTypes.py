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

print(f"2.1 Integer: {age} -> {type(age)}")       # Output : 2.1 Integer: 29 -> <class 'int'>
print(f"2.2 Float: {height} -> {type(height)}")   # Output : 2.2 Float: 162.5 -> <class 'float'>
print(f"2.3 Complex: {imaginary_num} -> {type(imaginary_num)}")   
# Output : 2.3 Complex: (3+5j) -> <class 'complex'>


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
# Output : 3.1 List: ['Python', 'React', 'Figma'] -> <class 'list'>
print(f"3.2 Tuple: {coordinates_tuple} -> {type(coordinates_tuple)}")
# Output : 3.2 Tuple: (48.81, 9.31) -> <class 'tuple'>
print(f"3.3 Range: {list(numbers_range)} -> {type(numbers_range)}")
# Output : 3.3 Range: [1, 2, 3, 4, 5] -> <class 'range'>


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
# Output : 4. Dictionary: {'name': 'Samar', 'role': 'Full-Stack Developer', 'experience_years': 3} -> <class 'dict'>

#---------------------------------------------------------------------------------------
# 5. Set Types: set, frozenset
#---------------------------------------------------------------------------------------
# Set: Unordered, UNINDEXED, and NO duplicate members allowed   ---> { , , }
unique_tags = {"python", "ui_ux", "python"}  # Duplicate 'python' will be removed automatically

# Frozenset: Just like a set, but completely immutable (unchangeable)   ---> frozenset ({ , })
frozen_tags = frozenset({"html", "css"})

print(f"5.1 Set: {unique_tags} -> {type(unique_tags)}") 
# Output : 5.1 Set: {'python', 'ui_ux'} -> <class 'set'>
print(f"5.2 Frozenset: {frozen_tags} -> {type(frozen_tags)}")
# Output : 5.2 Frozenset: frozenset({'css', 'html'}) -> <class 'frozenset'>

#---------------------------------------------------------------------------------------
# 6. Boolean Type: bool
#---------------------------------------------------------------------------------------
# Represents one of two values: True or False
is_backend_developer = True
is_student = False

print(f"6.1 Boolean True: {is_backend_developer} -> {type(is_backend_developer)}")
#  Output:  6.1 Boolean True: True -> <class 'bool'>
print(f"6.2 Boolean False: {is_student} -> {type(is_student)}")
#   Output: 6.2 Boolean False: False -> <class 'bool'>

#---------------------------------------------------------------------------------------
# 7. Binary Types: bytes, bytearray, memoryview
#---------------------------------------------------------------------------------------
# Used for handling raw binary data (e.g., files, network streams)

byte_data = b"Hello"                 # Bytes (Immutable)
mutable_bytes = bytearray(5)         # Bytearray (Mutable)
mem_view = memoryview(byte_data)     # Allows access to internal buffer data

print(f"7.1 Bytes: {byte_data} -> {type(byte_data)}")   
 #  Output: 7.1 Bytes: b'Hello' -> <class 'bytes'>
print(f"7.2 Bytearray: {mutable_bytes} -> {type(mutable_bytes)}")
#  Output: 7.2 Bytearray: bytearray(b'\x00\x00\x00\x00\x00') -> <class 'bytearray'>
print(f"7.3 Memoryview: {mem_view} -> {type(mem_view)}")
#  Output: 7.3 Memoryview: <memory at 0x00000238C9B85F00> -> <class 'memoryview'>

#---------------------------------------------------------------------------------------
# 8. None Type: NoneType
#---------------------------------------------------------------------------------------
# Represents the absence of a value or a null value
database_connection = None
print(f"8. None Type: {database_connection} -> {type(database_connection)}")   
 # Output : 8. None Type: None -> <class 'NoneType'>