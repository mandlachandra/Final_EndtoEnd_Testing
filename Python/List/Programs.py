#diff b/w list.append() and list.extend()
#list.append() ->Adds the whole object x as a single element to the end of the list
# fruits = ["apple","mango"]
# fruits.append(["cherry","kiwi"])
# print(fruits)
# output = ['apple', 'mango', ['cherry', 'kiwi']]

#List.extend() - Takes an iterable(list,tuple,set) and adds each element individually to the list
# fruits = ["apple","orange"]
# fruits.extend(["mango","banana"])
# print(fruits)

#How do you remove duplicates from list
#1.using set
# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# unique_fruits = list(set(fruits))
# print(unique_fruits)

#2.using dict.fromkeys()
# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# unique_fruits = list(dict.fromkeys(fruits))
# print(unique_fruits)

#3.Using a loop (Keeps order, more manual)
# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# unique_fruits = []
# for fruit in fruits:
#     if fruit not in unique_fruits:
#         unique_fruits.append(fruit)
# print(unique_fruits)

#How to reverse a list in python #done
#1.using reverse
# numbers = [1,2,3,4,6]
# numbers.reverse()
# print(numbers)

#2.using [::-1] = #done
# numbers1 = [1,2,3,4,6,9]
# reversed_list = numbers1[::-1]
# print(reversed_list)

#3.using reversed()
# numbers11 = [3,4,56,82,2]
# reversed_list = reversed(numbers11)
# print(list(reversed_list))

#how do you remove all occurrence of a specific element
#using list comprehension
# nums = [1,2,3,4,5,6,7,8,2,6,2]
#
# nums = [x for x in nums if x!=2]
#
# print(nums)

#using while loop

# nums = [1,2,3,4,5,6,7,8,2,6,2]
#
# while 2 in nums:
#     nums.remove(2)
#
# print(nums)

#using filter
# nums = [1,2,3,4,5,6,7,8,2,6,2]
# nums = list(filter(lambda x : x!=2,nums))
# print(nums)

# nums = [1, 2, 3, 2, 4, 2, 5, 3, 3, 3]
# from collections import Counter
#
# counter = Counter(nums)
#
# most_common = counter.most_common(1)[0][0]
# frequency = counter.most_common(1)[0][1]
#
# print(f"most frequent element: {most_common} (occurs {frequency} times)")

#when would you use deque instead of list
#you will use deque instead of list when you need fast appends and pops from both ends of a sequence
#
# from collections import deque
#
# d = deque([1,2,3])
#
# #append at both ends
# d.append(4)
# d.appendleft(0)
#
# #pop from both sides
# # d.pop()
# # d.popleft()
#
# print(d)

#find common elements in 2 list

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# common_elements = list(set(list1) & set(list2))
# print(common_elements)

#Find duplicates in list

# from collections import Counter
#
# my_list = [1, 2, 3, 4, 2, 3, 5, 3]
#
# count = Counter(my_list)
# duplicates = [item for item, freq in count.items() if freq>1]
# print("duplicates:",duplicates)

#reverse a list =done
# my_list = [1, 2, 3, 4, 5]
# reversed_list = my_list[::-1]
# print(reversed_list)

#using loop
# my_list = [1, 2, 3, 4, 5]
# reversed_list = []
# for item in my_list:
#     reversed_list.insert(0,item)
#
# print(reversed_list)

#merge 2 sorted list = done
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
#
# sorted_list = sorted(list1+list2)
# print(sorted_list)
#remove duplicates from list without using set = done
# numbers = [1, 2, 2, 3, 4, 4, 5, 1]
# new_list = []
# for num in numbers:
#     if num not in new_list:
#         new_list.append(num)
#
# print(new_list)

