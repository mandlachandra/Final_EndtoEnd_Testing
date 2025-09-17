# 1. Basic if statement
# x = 10
# if x > 5:
#     print("x is greater than 5")
#
#
# ✅ Runs only if condition is True.
#
# 2. if + else
# x = 3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")
#
#
# ✅ else is the fallback if condition fails.
#
# 3. if + elif
# x = 10
# if x == 5:
#     print("x is 5")
# elif x == 10:
#     print("x is 10")
#
#
# ✅ elif is checked if previous if was False.
#
# 4. if + elif + else
# x = 20
# if x == 10:
#     print("x is 10")
# elif x == 20:
#     print("x is 20")
# else:
#     print("x is something else")
#
#
# ✅ Covers multiple conditions and a fallback.
#
# 5. Multiple elif conditions
# marks = 75
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")
#
#
# ✅ Checks multiple levels.
#
# 6. Nested if (if inside another if)
# x = 15
# if x > 10:
#     if x < 20:
#         print("x is between 10 and 20")
#
#
# ✅ Used for hierarchical decisions.
#
# 7. Using logical operators (and, or, not)
# age = 25
# if age >= 18 and age <= 60:
#     print("Eligible")
# else:
#     print("Not eligible")
#
#
# ✅ Combines multiple conditions.
#
# 8. Ternary operator (single-line if else)
# x = 7
# result = "Even" if x % 2 == 0 else "Odd"
# print(result)
#
#
# ✅ Compact way to write if-else.
#
# 9. Multiple conditions in single if
# x = 10
# y = 20
# if x < 15 and y > 15:
#     print("Both conditions are true")
#
# 10. Checking membership (in, not in)
# fruits = ["apple", "banana", "mango"]
#
# if "apple" in fruits:
#     print("Apple is available")
# elif "orange" in fruits:
#     print("Orange is available")
# else:
#     print("No match found")
#
# 11. Using if with type checking
# data = 100
# if isinstance(data, int):
#     print("Integer")
# elif isinstance(data, str):
#     print("String")
# else:
#     print("Other type")
#
# 12. Chained comparisons
# x = 15
# if 10 < x < 20:
#     print("x is between 10 and 20")
#
#
# ✅ Cleaner than using and.
#
# 13. pass inside if
# x = 10
# if x > 5:
#     pass  # Placeholder (does nothing for now)
# else:
#     print("x <= 5")
#
#
# ✅ Useful in frameworks where logic is pending.
#
# 14. if with function return
# def check(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# print(check(7))
#
#
# ⚡ So in summary:
#
# if → single condition
#
# if + else → two possibilities
#
# if + multiple elif + else → multi-way decision
#
# Works with logical operators, nested conditions, membership, type-checking, chained comparisons, ternary operator, etc.