"""
===========================================================
Python Data Structures: Lists vs Tuples vs Arrays vs Dictionaries
===========================================================

This file explains the key differences between:
1. Lists
2. Tuples
3. Arrays (from the array module)
4. Dictionaries

We compare them in terms of:
- Mutability
- Performance
- Type flexibility
- Memory usage
- When to use each one
"""
# ===========================================================
# 1. LISTS
# ===========================================================

"""
LISTS:
- Ordered collection
- Mutable (can be changed)
- Can store mixed data types
- Most commonly used data structure in Python
"""

# Creating a list
my_list = [1, 2, 3, "hello", 4.5]

print("Original list:", my_list)

# Lists are mutable (you can change elements)
my_list[0] = 100
print("After modification:", my_list)

# Adding elements
my_list.append("new item")
print("After append:", my_list)

# Removing elements
my_list.remove(2)
print("After removing 2:", my_list)

# Lists allow mixed data types
print("List data types:", [type(item) for item in my_list])


# ===========================================================
# 2. TUPLES
# ===========================================================

"""
TUPLES:
- Ordered collection
- Immutable (cannot be changed after creation)
- Can store mixed data types
- Faster and safer than lists for fixed data
"""

# Creating a tuple
my_tuple = (1, 2, 3, "hello", 4.5)

print("\nOriginal tuple:", my_tuple)

# Accessing elements (allowed)
print("First element:", my_tuple[0])

# Attempting to modify a tuple will cause an error
# remove the comment below to check !

#my_tuple[0] = 100

# Tuples allow mixed data types
print("Tuple data types:", [type(item) for item in my_tuple])

"""
WHY USE TUPLES?
- Data should not change (coordinates, configuration)
- Safer (prevents accidental modification)
- Slightly faster than lists
"""


# ===========================================================
# 3. ARRAYS
# ===========================================================

"""
ARRAYS (from array module):
- Ordered collection
- Mutable
- Stores ONLY ONE data type
- More memory-efficient than lists
"""

import array

# Creating an integer array
# 'i' means signed integer
my_array = array.array('i', [1, 2, 3, 4, 5])

print("\nOriginal array:", my_array)

# Modifying array elements
my_array[0] = 100
print("After modification:", my_array)

# Adding elements
my_array.append(6)
print("After append:", my_array)

# Arrays DO NOT allow mixed types
# Uncommenting the line below will raise a TypeError
# my_array.append("hello")

"""
COMMON ARRAY TYPE CODES:
'i' -> int
'f' -> float
'd' -> double
'b' -> signed char
"""

# ===========================================================
# 4. DICTIONARIES
# ===========================================================
"""
DICTIONARIES:
- Unordered collection (Python 3.7+ maintains insertion order)
- Mutable
- Stores key-value pairs
- Keys must be immutable (numbers, strings, tuples)
- Values can be any type
"""

# Creating a dictionary
my_dict2 = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "new Dict":[],

}

my_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "new Dict":[1,2 []],
    "1": my_dect2
}

print("\nOriginal dictionary:", my_dict)

# Accessing values by key
print("Name:", my_dict["name"])

# Adding a new key-value pair
my_dict["grade"] = "A"
print("After adding grade:", my_dict)

# Modifying a value
my_dict["age"] = 26
print("After modifying age:", my_dict)

# Removing a key-value pair
del my_dict["is_student"]
print("After removing 'is_student':", my_dict)

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")


# ===========================================================
# 5. COMPARISON SUMMARY
# ===========================================================
"""
---------------------------------------------------------------
Feature          | List        | Tuple       | Array      | Dictionary
---------------------------------------------------------------
Mutable          | Yes         | No          | Yes        | Yes
Ordered          | Yes         | Yes         | Yes        | Yes (3.7+)
Mixed Types      | Yes         | Yes         | No         | Values Yes, Keys immutable
Indexed          | Yes         | Yes         | Yes        | No (key-value access)
Performance      | Medium      | Fast        | Fast       | Fast (hash table)
Memory Efficient | No          | Yes         | Yes        | Medium
Common Usage     | General     | Fixed data  | Numeric    | Key-value mapping
---------------------------------------------------------------
"""


# ===========================================================
# 6. WHEN TO USE WHAT?
# ===========================================================
"""
Use LISTS when:
- You need flexibility
- You need to change data often
- You want mixed data types

Use TUPLES when:
- Data should not change
- You want safety and performance
- Represent fixed structures (x, y coordinates)

Use ARRAYS when:
- Working with numeric data
- Memory efficiency matters
- All elements are same type

Use DICTIONARIES when:
- You need to map keys to values
- Fast lookup by key is important
- Order matters (Python 3.7+)
"""

print("\n--- End of demonstration ---")
