#1. Sort a List of Tuples by Second Element
# data = [(1, 3), (4, 1), (2, 2)]
# sorted_data = sorted(data, key=lambda x:x[1])
# print(sorted_data)

#2.Sort Tuples Alphabetically by First Element (String)
# data = [("banana", 2), ("apple", 5), ("mango", 3)]
# sorted_data = sorted(data,key=lambda x : x[0])
# print(sorted_data)

#3. Sort Tuples by Sum of Elements
# data = [(1, 4), (2, 2), (3, 1)]
# sorted_data = sorted(data,key=lambda x:sum(x))
# print(sorted_data)

    #4. Sort Tuples by Length of String Element
    # data = [("elephant", 3), ("dog", 1), ("horse", 2)]
    # sorted_data = sorted(data, key=lambda x: len(x[0]))
    # print(sorted_data)

# #5. Sort Tuples in Descending Order by Numeric Field
# data = [("apple", 10), ("banana", 5), ("cherry", 15)]
# sorted_data = sorted(data, key=lambda x:x[1],reverse=True)
# print(sorted_data)

#what are namedtuple in python ?
# A named tuple in python is a lightweight, immutable data structure thats like a regular tuple
# but with named fields so you can access elements using dot notation instead of only by index
#
# it comes from collections module

# from collections import namedtuple
#
# Person = namedtuple("person",["name","age","city"])
# p = Person("john",25,"new york")
# print(p.name)
# print(p.age)
# print(p.city)
