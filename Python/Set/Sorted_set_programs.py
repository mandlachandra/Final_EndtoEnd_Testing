#1. Sort a Set of Integers
# nums = {6,4,1,3,8,9}
# sorted_nums = sorted(nums)
# print(sorted_nums)

nums = {3,5,6,1,8,6}
sorted_nums = sorted(nums)
print(sorted_nums)

#2. Sort a Set of Strings Alphabetically
# fruits = {'banana','apple','kiwi','fig'}
# sorted_fruits = sorted(fruits)
# print(sorted_fruits)

#3. Sort a Set of Strings by Length
# words = {'banana','grapes','melons','jack'}
# sorted_words = sorted(words,key=len)
# print(sorted_words)

#4. Sort Set of Tuples by Second Element
# pairs = {(1,3),(2,1),(3,2)}
# sorted_pairs = sorted(pairs,key=lambda x : x[1])
# print(sorted_pairs)

#Convert List to Set, Remove Duplicates, and Sort
# data = [5,2,3,5,3,4,5,8]
# unique_sorted = sorted(set(data))
# print(unique_sorted)

#1: Removing duplicates from a list
# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# unique_fruits = list(set(fruits))
# print(unique_fruits)
#
# 2: Removing duplicates while keeping order
fruits = ["apple", "banana", "apple", "cherry", "banana"]
unique_fruits = list(dict.fromkeys(fruits))
print(unique_fruits)