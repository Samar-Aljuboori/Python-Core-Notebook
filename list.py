
#6-Python List Data Type 
#------------------------#
ages = [19, 26, 29]
print(ages)                  #[19, 26, 29]

# Access List Items (Posative Indexing)
#---------------------------------------
skills = ["React", "Java", "Python"]  
print(skills[0])               #React
print(skills[2])               # Python


# Access List Items (Nagative Indexing)
#---------------------------------------
skills = ["React", "Java", "Python"]  
print(skills[-3])               #Python
print(skills[-1])               # React



#List Items of Different Types
#-----------------------------
student = ['Jack', 32, 'Computer Science', [2, 4]]
print(student)                  #['Jack', 32, 'Computer Science', [2, 4]]

# an empty list
#---------------
empty_list = []
print(empty_list)               #[]


#Slicing of a List in Python
#---------------------------
my_list = ['p', 'y', 't', 'h', 'o', 'n']
print("my_list =", my_list)                         #my_list = ['p', 'y', 't', 'h', 'o', 'n']

# from index 1 to index 4 (index 5 is not included)
print("my_list[2: 5] =", my_list[1: 4])             #my_list[2: 5] = ['y', 't', 'h']

# from index 2 to index -3 (index -2 is not included)
print("my_list[2: -2] =", my_list[2: -2])           #my_list[2: -2] = ['t', 'h']

# from index 0 to index 2 (index 3 is not included)
print("my_list[0: 3] =", my_list[0: 3])             #my_list[0: 3] = ['p', 'y', 't']



#Omitting Start and End Indices in Slicing
#-----------------------------------------
my_list = ['p', 'y', 't', 'h', 'o', 'n']
print("my_list =", my_list)                  #my_list = ['p', 'y', 't', 'h', 'o', 'n']

# from index 5 to last
print("my_list[5: ] =", my_list[5: ])        #my_list[5: ] = ['n']

# from the first item to index -5
print("my_list[: -4] =", my_list[: -4])      #my_list[: -4] = ['p', 'y']

# from start to end items
print("my_list[:] =", my_list[:])           #my_list[:] = ['p', 'y', 't', 'h', 'o', 'n']



#Add Elements to a Python List ---> .append() 
#---------------------------------------------
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)               #Original List: ['apple', 'banana', 'orange']

fruits.append('cherry')

print('Updated List:', fruits)                #Updated List: ['apple', 'banana', 'orange', 'cherry']



#Add Elements at the Specified Index
#-------------------------------------
fruits = ['apple', 'banana', 'orange']
print("Original List:", fruits)              #Original List: ['apple', 'banana', 'orange']

fruits.insert(2, 'cherry')

print("Updated List:", fruits)              #Updated List: ['apple', 'banana', 'cherry', 'orange']


#Add Elements to a List From Other Iterables ---> . extend() 
numbers = [1, 3, 5]
print('Numbers:', numbers)                   #Numbers: [1, 3, 5]

even_numbers  = [2, 4, 6]
print('Even numbers:', even_numbers)         #Even numbers: [2, 4, 6]

# adding elements of one list to another
numbers.extend(even_numbers)

print('Updated Numbers:', numbers)          #Updated Numbers: [1, 3, 5, 2, 4, 6]


#Change List Items
#------------------
colors = ['Red', 'White', 'Blue']
print('Original List:', colors)           #Original List: ['Red', 'White', 'Blue']

colors[0] = 'Purple'

colors[2] = 'Black'

print('Updated List:', colors)            #Updated List: ['Purple', 'White', 'Black']

#Remove an Item From a List
#---------------------------
numbers = [8,6,12,14]

# remove 4 from the list
numbers.remove(12)

print(numbers)                             #[8,6,14]


#Remove One or More Elements of a List
#-------------------------------------
names = ['Jack', 'Paul', 'Hinray', 'Sara', 'Laura']

# delete the item at index 1
del names[1]
print(names)                             #['Jack', 'Hinray', 'Sara', 'Laura']

# delete items from index 1 to index 2
del names[1: 3]
print(names)                             #['Jack', 'Laura']

# delete the entire list
#del names

# Error! List doesn't exist.
#print(names)                            #Traceback (most recent call last):
                                        #NameError: name 'names' is not defined. Did you mean: 'ages'?



#Python List Length
#------------------
fruits = ['banan', 'orange', 'kiwi' , 'mango']

print('Total Fruits :', len(fruits))            #Total Fruits :4



#Iterating Through a List
#-------------------------
fruits = ['banan', 'orange', 'kiwi' , 'mango']
for fruit in fruits :
    print(fruit)                              #banan
                                              #orange
                                              #kiwi
                                              #mango






# Functions with List
#----------------------
skills = ["Python", "JavaScript", "Figma"]
print(f"Original List: {skills}\n")                           #Original List: ["Python", "JavaScript", "Figma"]

# 1. append() - Adds a single item to the end of the list
skills.append("React")
print(f"1. After append(): {skills}")                          #1. After append(): ["Python", "JavaScript" , "Figma" , "React"]

# 2. extend() - Adds multiple items (from another list) to the end
new_tools = ["PHP", "MySQL"]
skills.extend(new_tools)
print(f"2. After extend(): {skills}")                           #2. After extend(): ["Python", "JavaScript" , "Figma" , "React" , "PHP", "MySQL"]

# 3. insert() - Inserts an item at a specified index
# Inserting "UI/UX" at the very beginning (Index 0)
skills.insert(0, "UI/UX")
print(f"3. After insert(): {skills}")                            #3. After insert(): ["UI/UX" , 'Python' , "JavaScript" , "Figma" , "React" , "PHP", "MySQL"]


# 4. remove() - Removes the first occurrence of a specific value
skills.remove("PHP")
print(f"4. After remove(): {skills}")                             #4. After remove(): ["UI/UX" , 'Python' , "JavaScript" , "Figma" , "React" , "MySQL"]

# 5. pop() - Removes and returns the item at the given index
# If no index is specified, pop() removes and returns the last item
removed_item = skills.pop(2)  # Removes index 2 (which is 'JavaScript' at this point)
print(f"5. After pop(2): {skills}")                                #5. After pop(2): ['UI/UX', 'Python', 'Figma', 'React', 'MySQL']
print(f"   The removed item was: {removed_item}")                 #The removed item was:JavaScript

# 6. index() - Returns the index (position) of the first matched item
figma_position = skills.index("Figma")
print(f"6. The index of 'Figma' is: {figma_position}")            #6. The index of 'Figma' is: 2

# 7. count() - Returns the number of times a value appears in the list
skills.append("Python")  # Adding a duplicate to demonstrate count
python_count = skills.count("Python")
print(f"7. 'Python' appears {python_count} times in the list.")     #7. 'Python' appears 2 times in the list.

# 8. sort() - Sorts the list items in ascending/alphabetical order
skills.sort()
print(f"8. After sort(): {skills}")                                  #8. After sort(): ['Figma', 'MySQL', 'Python', 'Python', 'React', 'UI/UX']

# 9. reverse() - Reverses the order of the items in the list
skills.reverse()
print(f"9. After reverse(): {skills}")                               #9. After reverse(): ['UI/UX', 'React', 'Python', 'Python', 'MySQL', 'Figma']

# 10. copy() - Returns a shallow copy (independent backup) of the list
skills_backup = skills.copy()
print(f"10. Backup list created successfully: {skills_backup}")      #10. Backup list created successfully: ['UI/UX', 'React', 'Python', 'Python', 'MySQL', 'Figma']

# 11. clear() - Removes all elements from the list completely
skills.clear()
print(f"11. After clear(): {skills}")                                #11. After clear(): []
# Output will be [] (empty list)

                                            