# 1. Basic for loop with a list
# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print(fruit)
#
#
# ✅ Iterates over list elements.
#
# 2. For loop with range()
# for i in range(5):
#     print(i)   # 0,1,2,3,4
#
#
# ✅ Useful when you want numbers in a sequence.
#
# 3. For loop with range(start, stop, step)
# for i in range(1, 11, 2):
#     print(i)   # 1,3,5,7,9
#
#
# ✅ Control start, stop, step values.
#
# 4. For loop with enumerate() (index + value)
# fruits = ["apple", "banana", "mango"]
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)
#
#
# ✅ Useful when you need both index and value.
#
# 5. For loop with dictionary
# person = {"name": "Sekhar", "age": 30, "city": "Hyderabad"}
#
# for key, value in person.items():
#     print(key, ":", value)
#
#
# ✅ Iterating over key-value pairs.
#
# 6. For loop with zip() (parallel iteration)
# names = ["Sekhar", "Anil", "Ravi"]
# scores = [90, 85, 78]
#
# for name, score in zip(names, scores):
#     print(name, score)
#
#
# ✅ Iterate multiple lists together.
#
# 7. Nested for loop
# for i in range(3):
#     for j in range(2):
#         print(f"i={i}, j={j}")
#
#
# ✅ Loop inside loop.
#
# 8. For loop with list comprehension
# squares = [x**2 for x in range(5)]
# print(squares)   # [0, 1, 4, 9, 16]
#
#
# ✅ Compact way to create new lists.
#
# 9. For loop with break and continue
# for i in range(10):
#     if i == 5:
#         break     # stops loop
#     if i % 2 == 0:
#         continue  # skips even numbers
#     print(i)
#
# 10. For loop with else
# for i in range(3):
#     print(i)
# else:
#     print("Loop finished without break")
#
#
# ✅ Runs else only if loop didn’t break.
#
# 11. For loop with sorted()
# nums = [4, 1, 7, 3]
# for n in sorted(nums):
#     print(n)
#
#
# ✅ Iterates in sorted order.
#
# 12. For loop with set()
# unique_nums = {1, 2, 3, 1, 2}
# for num in unique_nums:
#     print(num)
#
#
# ✅ Removes duplicates automatically.
#
# 13. Infinite loop (with break condition)
# for i in iter(int, 1):  # tricky, creates infinite loop
#     print("Hello")
#     break
#
#
# ✅ Rare, but shows iter() usage.
#
# 14. For loop with zip and enumerate together
# names = ["Sekhar", "Anil", "Ravi"]
# scores = [90, 85, 78]
#
# for i, (name, score) in enumerate(zip(names, scores), start=1):
#     print(f"{i}. {name} -> {score}")
#
#
# 🔥 These are the main variations of for loop in Python that cover:
#
# List, dict, set
#
# Index + value
#
# Multiple lists
#
# Nested loops
#
# Comprehensions
#
# Break/continue/else
#
# Sorting and unique handling