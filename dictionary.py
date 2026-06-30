#The Ultimate Master Blueprint for Python Dictionaries
 
#---------------------------------------------------------------------------------------
# 1. Dictionary Basics & Initialization
#---------------------------------------------------------------------------------------
# Dictionaries store data in Key:Value pairs. They are Ordered, Changeable, and 
# DO NOT allow duplicate keys (the new value overwrites the old one).

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2026  # Duplicate key: 2026 will overwrite 1964
}
print("1. Dictionary Overwrite:", car_dict) 
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2026}


#---------------------------------------------------------------------------------------
# 2. Accessing Items (The Standard way vs The Safe way)
#---------------------------------------------------------------------------------------
smart_watch = {"brand": "Apple", "series": "Ultra", "price": 799}

# 2.1 Using Square Brackets []: Throws a KeyError if the key doesn't exist
print("\n2.1 Access via []:", smart_watch["series"])     # Output: Ultra

# 2.2 Using get(): Safe approach. Returns 'None' instead of crashing if key is missing
print("2.2 Access via get():", smart_watch.get("color")) # Output: None


#---------------------------------------------------------------------------------------
# 3. Adding and Modifying Elements
#---------------------------------------------------------------------------------------
laptop_dict = {"brand": "Dell", "ram": "16GB"}

# If the key exists, it updates the value. If not, it creates a new pair.
laptop_dict["ram"] = "32GB"       # Modifying
laptop_dict["storage"] = "1TB"    # Adding
print("\n3. After Modifications:", laptop_dict) 
# Output : 3. After Modifications: {'brand': 'Dell', 'ram': '32GB', 'storage': '1TB'}

#---------------------------------------------------------------------------------------
# 4. Removing Items (pop, popitem, clear, and the powerful 'del')
#---------------------------------------------------------------------------------------
devices = {"phone": "iPhone", "tablet": "iPad", "screen": "OLED", "audio": "AirPods"}

# 4.1 pop(key): Removes the specified key and returns its value
removed_phone = devices.pop("phone")

# 4.2 popitem(): Removes and returns the LAST inserted key-value pair  تحذف اخر عنصر موجود بالقاموس
removed_last = devices.popitem()

# 4.3 del keyword: Deletes a specific item by its key
del devices["tablet"]
print("\n4.3 Remaining after pop, popitem, and del:", devices) # Output: {'screen': 'OLED'}

# 4.4 del completely: Destroys the whole dictionary from memory
temp_dict = {"temp": "data"}
del temp_dict
# print(temp_dict) ⚠️ This will raise a NameError because temp_dict is completely deleted!

# 4.5 clear(): Empties the whole dictionary but keeps the empty structure alive (returns {})
devices.clear()
print("4.5 After clear():", devices)                      # Output: {}


#---------------------------------------------------------------------------------------
# 5. Extracting Keys, Values, and Items (Essential for Loops)
#---------------------------------------------------------------------------------------
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# 5.1 Looping through keys using .keys() method explicitly
print("\n5.1 Looping through keys:")
for x in thisdict.keys():
    print(x)
#Output : 5.1 Looping through keys:
         #brand
         #model
         #year

# 5.2 Looping through values using .values() method explicitly
print("\n5.2 Looping through values:")
for x in thisdict.values():
    print(x)
# Output : 5.2 Looping through values:
           #Ford
           #Mustang
           #1964

# 5.3 Looping through both keys and values using .items()
print("\n5.3 Looping through items (keys and values):")
for key, value in thisdict.items():
    print(f" - {key}: {value}")
# Output : 5.3 Looping through items (keys and values):
          #- brand: Ford
          #- model: Mustang
          #- year: 1964

#---------------------------------------------------------------------------------------
# 6. Copying Dictionaries (Side-by-Side Comparison)
#---------------------------------------------------------------------------------------
# 6.1 Copy using the .copy() method
mydict1 = thisdict.copy()
print("\n6.1 Method 1 (.copy()):", mydict1)
# Output : 6.1 Method 1 (.copy()): {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# 6.2 Copy using the dict() constructor function
mydict2 = dict(thisdict)
print("6.2 Method 2 (dict()):", mydict2)
# Output : 6.2 Method 2 (dict()): {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#---------------------------------------------------------------------------------------
# 7. Nested Dictionaries (Complex Data Structures)
#---------------------------------------------------------------------------------------
# 7.1 Creating separate dictionaries first, then combining them into one
child1 = {"name" : "Emil", "year" : 2004}
child2 = {"name" : "Tobias", "year" : 2007}
child3 = {"name" : "Linus", "year" : 2011}

myfamily1 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print("\n7.1 Nested via Combination:", myfamily1)
# Output : 7.1 Nested via Combination: {'child1': {'name': 'Emil', 'year': 2004}, 
# 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


# 7.2 Creating everything directly inside one nested dictionary
myfamily2 = {
  "child1" : {"name" : "Emil", "year" : 2004},
  "child2" : {"name" : "Tobias", "year" : 2007},
  "child3" : {"name" : "Linus", "year" : 2011}
}
print("7.2 Nested via Direct Creation:", myfamily2)
# Output : 7.2 Nested via Direct Creation: {'child1': {'name': 'Emil', 'year': 2004},
#  'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}



# 7.3 Advanced: Looping through all keys and values of nested dictionaries
print("\n7.3 Looping through Nested Dictionaries:")
for x, obj in myfamily2.items():
    print(f"Family Member Key: {x}")
    for y in obj:
        print(y + ':', obj[y])
# Output : 7.3 Looping through Nested Dictionaries:
          #Family Member Key: child1
          #name: Emil
          #year: 2004
          #Family Member Key: child2
          #name: Tobias
          #year: 2007
          #Family Member Key: child3
          #name: Linus
          #year: 2011

#---------------------------------------------------------------------------------------
# 8. Advanced Methods (.update() and .setdefault())
#---------------------------------------------------------------------------------------
# 8.1 setdefault(): Returns value of key. If key doesn't exist: inserts key with value
office_supplies = {"pens": 10, "papers": 50}
markers_count = office_supplies.setdefault("markers", 5) 
print("\n8.1 setdefault() result:", office_supplies)
# Output : 8.1 setdefault() result: {'pens': 10, 'papers': 50, 'markers': 5}

# 8.2 fromkeys(): Creates a dictionary from a sequence of keys with a shared single value
categories = ["HTML", "CSS", "Python"]
status_dict = dict.fromkeys(categories, "Completed")
print("8.2 fromkeys() result:", status_dict)
# Output : 8.2 fromkeys() result: {'HTML': 'Completed', 'CSS': 'Completed', 'Python': 'Completed'}


# 8.3 update(): Updates the dictionary with specified key-value pairs
inventory = {"apples": 10, "bananas": 5}
new_delivery = {"bananas": 20, "oranges": 15} 
inventory.update(new_delivery)
print("8.3 After update():", inventory) 
# Output: {'apples': 10, 'bananas': 20, 'oranges': 15}


# --------------------------------------------------------------------------------------
# QUICK REFERENCE: Summary of All Built-in Dictionary Methods
# --------------------------------------------------------------------------------------
# clear()      -> Removes all the elements from the dictionary
# copy()       -> Returns a copy of the dictionary
# fromkeys()   -> Returns a dictionary with the specified keys and value
# get()        -> Returns the value of the specified key (Safe)
# items()      -> Returns a list containing a tuple for each key value pair
# keys()       -> Returns a list containing the dictionary's keys
# pop()        -> Removes the element with the specified key
# popitem()    -> Removes the last inserted key-value pair
# setdefault() -> Returns value of key. If key doesn't exist: inserts key with value
# update()     -> Updates the dictionary with the specified key-value pairs
# values()     -> Returns a list of all the values in the dictionary
# --------------------------------------------------------------------------------------