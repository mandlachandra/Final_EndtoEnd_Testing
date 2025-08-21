#1.count frequency of each character in a string
# s = "mandlachandrasekhar"
# freq = {}
#
# for char in s:
#     if char in freq:
#         freq[char] +=1
#
#     else:
#         freq[char] =1
#
# print(freq)

#merge 2 dictionary
d1 = {"a":1,"b":3}
d2 = {"b":34,"c":45}

# d1.update(d2)
# print(d1)
merged = d1 | d2
print(merged)
#remove a key value pair
# person = {"name":"sekhar","age":30}
# removed_value = person.pop("age")
# print("removed:",removed_value)
# print("updated dict:",person)
#
# #get all keys and values separately
# d = {"x":10,"y":30}
# print("keys:",list(d.keys()))
# print("values:",list(d.values()))

# 1: Basic dictionary inversion
#
# my_dict = {"a": 1, "b": 2, "c": 3}
# inverted = {value: key for key , value in my_dict.items()}
# print(inverted)
#
# #Common keys in 2 dictionaries
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 20, "c": 30, "d": 40}
#
# # common_keys = dict1.keys() & dict2.keys()
# # print(common_keys)
#
# common_items = dict1.items() & dict2.items()
# print(common_items)
#
# from collections import Counter
# sentence = "Apple Banana apple orange banana apple"
# word_count = Counter(sentence.split())
# print(word_count)

# #How do dictionaries work internally in python
# In python dictionaries are implemented as hash tables and their internal working is all about
# hasing,bucktes and collision handling

#Dictionary basic
# my_dict = {"name": "Alice", "age": 25}
# keys must be hashable (immutable like str,int, tuple etc)
#
# #Internal data structure
# Internally python dictionary is:
# An array of "buckets":
# Each bucket holds:
# 1.The hash of the key
# 2.The key itself
# 3.The value

# Index  |  Hash  |  Key   |  Value
# ---------------------------------
#   0    | 123456 | "name" | "Alice"
#   1    | 987654 | "age"  | 25
#   2    |   ...  |  ...   | ...
#
# hash("abc") == hash("xyz")  # Rare, but possible
#
# When collisions happen, Python uses open addressing (specifically perturbation probing):
#
# It tries the next position in a pseudo-random sequence until it finds:
#
# An empty slot (for insert).
#
# The matching key (for lookup).

# 5. Resizing
#
# If dictionary load factor > ~2/3 (too full), Python resizes:
#
# Creates a new larger table (usually ×2 size).
#
# Rehashes all keys into the new table.
#
# This keeps operations efficient.

#How do you merge 2 dictionaries
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
#
# dict1.update(dict2)  # dict1 is modified in place
# print(dict1)
# # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# #How do you sort a dictionary by key or by value
# my_dict = {'c':3,'b':4,'a':6}
#
# sorted_by_key = dict(sorted(my_dict.items()))
# print(sorted_by_key)
#
# #my_dict_items = returns (key,value) pairs
# sorted() ->sorts tuples by the first element (key) by default

#How do you check if key exists in a dictionary

# my_dict = {'a':2,'b':4,'c':9}
#
# if 'a' in my_dict:
#     print("key exists")
# else:
#     print("no key")

#what are dictionary comprehensions with examples
#A dictionary comprehension is a comcise way to create dictionaries using a single line of code
# similar to list comprehensions but with key-value pairs

# squares = {x:x**2 for x in range(5)}
# print(squares)


#Filtering with if Condition
# even_squares = {x:x**2 for x in range(10) if x%2==0}
# print(even_squares)

#Swapping Keys and Values
# original = {'a':3,'c':8,'g':9}
# inverted = {v: k for k, v in original.items()}
# print(inverted)

#how do you remove key from dictionary
original = {'a':3,'c':8,'g':9}

# value = original.pop('a')
# print(original)

del original['a']
print(original)





