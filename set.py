# DESCRIPTION: The Ultimate Comprehensive Guide to Python Sets (All Methods & Theory)
#---------------------------------------------------------------------------------------
# 1. What is a Set? (Characteristics)
#---------------------------------------------------------------------------------------
# A Set is a collection which is:
# - Unordered: The items do not have a defined order, they can appear differently each time.
# - Unindexed: You CANNOT access items using index numbers like lists [0].
# - No Duplicates: Every element must be unique. Duplicate values are filtered out.

# Creating a set of fruits
fruits_set = {"apple", "banana", "cherry", "apple"}
print("1. Original Set (Duplicates removed):", fruits_set)
# Output: {'banana', 'cherry', 'apple'} (Order may vary, duplicate 'apple' is gone)


# NOTE: How to create an EMPTY set?
# empty_set = {}  Wrong! This creates an empty Dictionary.
empty_set = set() #  Correct way!    ---> set()


#---------------------------------------------------------------------------------------
# 2. Accessing & Checking Items
#---------------------------------------------------------------------------------------
cars_set = {"BMW", "Tesla", "Toyota", "Ford"}

# Since sets are unindexed, we use a 'for' loop to iterate through them:
print("\n2.1 Iterating through cars_set:")
for car in cars_set:
    print(f" - {car}")
    # Output : 2.1 Iterating through cars_set:
    # - Tesla
    # - Toyota
    # - BMW
    # - Ford

# Checking if an item exists using 'in' or 'not in' keywords
print("\n2.2 Checking item existence:")                    # Output : 2.2 Checking item existence:
print("Is 'Tesla' in cars?", "Tesla" in cars_set)          # Output: True
print("Is 'Audi' not in cars?", "Audi" not in cars_set)     # Output: True


#---------------------------------------------------------------------------------------
# 3. Adding Items ---> (add(), update())
#---------------------------------------------------------------------------------------
colors_set = {"red", "green"}

# 3.1 add(): Adds a single element to the set
colors_set.add("blue")
print("\n3.1 After add():", colors_set)        # Output: {'red', 'green', 'blue'}

# 3.2 update(): Adds multiple elements (from a list, tuple, or another set)
more_colors = ["yellow", "purple", "red"]         # 'red' is a duplicate
colors_set.update(more_colors)
print("3.2 After update():", colors_set)          # Output: {'yellow', 'purple', 'blue', 'green', 'red'}


#---------------------------------------------------------------------------------------
# 4. Removing Items (remove, discard, pop, clear)
#---------------------------------------------------------------------------------------
tech_companies = {"Google", "Apple", "Microsoft", "Amazon", "Meta"}

# 4.1 Removes an item. Raises a KeyError if the item doesn't exist   ---> remove()
#  حذف مع اظهار  خطأ   عندما  يكن العنصر غير موجود

tech_companies.remove("Meta")

# 4.2 Removes an item. Does NOT raise an error if the item is missing   ---> discard() 
#  حذف بدون اظهار اي خطأ حتئ لو لم يكن العنصر موجود

tech_companies.discard("Netflix")            # 'Netflix' is not there, but code won't crash

# 4.3 Removes and returns a RANDOM item (because sets are unordered)   ---> pop()  حذف عشوائي
removed_item = tech_companies.pop()
print(f"\n4.3 pop() removed: '{removed_item}' | Remaining: {tech_companies}")
# Output : 4.3 pop() removed: 'Apple' | Remaining: {'Google', 'Microsoft', 'Amazon'}

# 4.4 clear(): Empties the entire set
tech_companies.clear()
print("4.4 After clear():", tech_companies)                 # Output: set()
#  Output : 4.4 After clear(): set()

#---------------------------------------------------------------------------------------
# 5. Mathematical Set Operations (The Core Power of Sets)
#---------------------------------------------------------------------------------------
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# 5.1 Union: Combines items from both sets (All unique items)
# Shortcut operator: A | B
print("\n5.1 +Union (A ∪ B):", set_A.union(set_B))      # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 5.2 Intersection: Returns items common to both sets
# Shortcut operator: A & B
print("5.2 Intersection (A ∩ B):", set_A.intersection(set_B))   # Output: {4, 5}

# 5.3 Difference: Returns items in set_A but NOT in set_B
# Shortcut operator: A - B
print("5.3 Difference (A - B):", set_A.difference(set_B))   # Output: {1, 2, 3}

# 5.4 Symmetric Difference: Returns items in either set, but NOT in both (opposite of intersection)
# Shortcut operator: A ^ B
print("5.4 Symmetric Difference (A Δ B):", set_A.symmetric_difference(set_B)) # Output: {1, 2, 3, 6, 7, 8}


#---------------------------------------------------------------------------------------
# 6. Advanced Evaluation Methods (Boolean Checks)
#---------------------------------------------------------------------------------------
sub_set = {"apple", "banana"}
main_set = {"apple", "banana", "cherry", "orange"}
other_set = {"grapes", "mango"}

# 6.1 issubset(): Checks if all items of a set are contained in another set
print("\n6.1 Is sub_set a subset of main_set?:", sub_set.issubset(main_set))   # Output: True

# 6.2 issuperset(): Checks if a set contains all items of another set
print("6.2 Is main_set a superset of sub_set?:", main_set.issuperset(sub_set)) # Output: True

# 6.3 isdisjoint(): Checks if two sets have NO common items (intersection is empty)
print("6.3 Are main_set and other_set disjoint?:", main_set.isdisjoint(other_set)) # Output: True


#---------------------------------------------------------------------------------------
# 7. In-Place Update Methods (Modifying the Original Set Directly)
#---------------------------------------------------------------------------------------
# Programiz highlights these methods which apply mathematical operations and modify the original set:

x = {"a", "b", "c"}
y = {"c", "d", "e"}

# 7.1 intersection_update(): Keeps only items found in both sets
x.intersection_update(y)
print("\n7.1 After intersection_update():", x)              # Output: {'c'}

# 7.2 difference_update(): Removes items found in the other set
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
set_1.difference_update(set_2)
print("7.2 After difference_update():", set_1)               # Output: {1}

# 7.3 symmetric_difference_update(): Keeps items from both, EXCEPT common ones
set_3 = {"BMW", "Audi"}
set_4 = {"Audi", "Tesla"}
set_3.symmetric_difference_update(set_4)
print("7.3 After symmetric_difference_update():", set_3)     # Output: {'BMW', 'Tesla'}