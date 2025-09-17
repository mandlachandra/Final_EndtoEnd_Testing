# 1. Extract numbers from a mixed list
# data = ["1", 332, "apple", 23, 44, 2, 1, "0", 5.6, "78.9"]
#
# numbers = []
# for item in data:
#     if isinstance(item, (int, float)):   # already number
#         numbers.append(item)
#     elif isinstance(item, str) and item.replace(".", "", 1).isdigit():
#         # handles "1", "0", "78.9"
#         numbers.append(float(item) if "." in item else int(item))
#
# print("Extracted numbers:", numbers)
#
#
# ✅ Output:
#
# Extracted numbers: [332, 23, 44, 2, 1, 5.6, 1, 78.9]
#
# 🔹 2. Separate data types into groups
# data = [10, "20", 30.5, {"a": 1}, (1, 2), [3, 4], {5, 6}, "python"]
#
# groups = {
#     "int": [],
#     "float": [],
#     "str": [],
#     "list": [],
#     "tuple": [],
#     "set": [],
#     "dict": []
# }
#
# for item in data:
#     groups[type(item).__name__].append(item)
#
# print(groups)
#
#
# ✅ Output:
#
# {'int': [10],
#  'float': [30.5],
#  'str': ['20', 'python'],
#  'list': [[3, 4]],
#  'tuple': [(1, 2)],
#  'set': [{5, 6}],
#  'dict': [{'a': 1}]}
#
# 🔹 3. Extract all integers inside nested structures
# data = [10, "abc", [20, "30", (40, "50")], {"x": 60, "y": "70"}]
#
# def extract_integers(obj):
#     result = []
#     if isinstance(obj, int):
#         result.append(obj)
#     elif isinstance(obj, str) and obj.isdigit():
#         result.append(int(obj))
#     elif isinstance(obj, (list, tuple, set)):
#         for i in obj:
#             result.extend(extract_integers(i))
#     elif isinstance(obj, dict):
#         for k, v in obj.items():
#             result.extend(extract_integers(k))
#             result.extend(extract_integers(v))
#     return result
#
# print("Extracted integers:", extract_integers(data))
#
#
# ✅ Output:
#
# Extracted integers: [10, 20, 30, 40, 50, 60, 70]
#
# 🔹 4. Find only strings with digits inside a mixed list
# data = ["abc", "123", 45, "python3", "45.6", {"key": "value"}]
#
# strings_with_digits = [x for x in data if isinstance(x, str) and any(ch.isdigit() for ch in x)]
# print(strings_with_digits)
#
#
# ✅ Output:
#
# ['123', 'python3', '45.6']
#
# 🔹 5. Convert all numeric strings to integers
# data = ["1", "hello", 23, "45", "3.5", 100]
#
# converted = []
# for item in data:
#     if isinstance(item, str):
#         if item.isdigit():
#             converted.append(int(item))
#         elif item.replace(".", "", 1).isdigit():
#             converted.append(float(item))
#         else:
#             converted.append(item)
#     else:
#         converted.append(item)
#
# print(converted)
#
#
# ✅ Output:
#
# [1, 'hello', 23, 45, 3.5, 100]
#
# 🔹 6. Flatten mixed nested list
# data = [1, [2, [3, "4"], "5"], "six", (7, 8)]
#
# def flatten(lst):
#     result = []
#     for item in lst:
#         if isinstance(item, (list, tuple)):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result
#
# print(flatten(data))
#
#
# ✅ Output:
#
# [1, 2, 3, '4', '5', 'six', 7, 8]
#
# 🔹 7. Extract only dictionary keys and values
# data = [{"id": 101, "name": "Alice"}, {"id": 102, "age": 25}, "string", 123]
#
# dict_keys = []
# dict_values = []
#
# for item in data:
#     if isinstance(item, dict):
#         dict_keys.extend(item.keys())
#         dict_values.extend(item.values())
#
# print("Keys:", dict_keys)
# print("Values:", dict_values)
#
#
# ✅ Output:
#
# Keys: ['id', 'name', 'id', 'age']
# Values: [101, 'Alice', 102, 25]
#
#
# ✨ Interview Takeaways:
#
# Use isinstance() to filter by type.
#
# For nested/mixed structures, recursion is the best approach.
#
# Always check string-to-number conversions (isdigit(), .replace(".", "", 1)).
#
# Grouping and flattening are very common interview challenges.