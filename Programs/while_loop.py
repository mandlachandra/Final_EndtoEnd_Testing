# 1. Basic while loop
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
#
#
# ✅ Runs until condition is False.
#
# 2. Infinite while loop
# while True:
#     print("Hello")
#     break   # exit condition (otherwise infinite)
#
#
# ✅ Used in servers, listeners, automation until a break.
#
# 3. while with else
# i = 1
# while i <= 3:
#     print(i)
#     i += 1
# else:
#     print("Loop finished without break")
#
#
# ✅ else executes if loop ends naturally (no break).
#
# 4. while with break
# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
#
#
# ✅ Exits loop immediately when condition met.
#
# 5. while with continue
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue   # skips printing 3
#     print(i)
#
#
# ✅ Skips the current iteration and moves to next.
#
# 6. Nested while loop
# i = 1
# while i <= 3:
#     j = 1
#     while j <= 2:
#         print(f"i={i}, j={j}")
#         j += 1
#     i += 1
#
#
# ✅ while loop inside another while.
#
# 7. Simulating for loop with while
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
#
# ✅ Equivalent to for i in range(5).
#
# 8. User input with while
# while True:
#     num = int(input("Enter a number (0 to exit): "))
#     if num == 0:
#         print("Exiting loop")
#         break
#     print("You entered:", num)
#
#
# ✅ Useful for interactive programs.
#
# 9. while with condition check (membership)
# fruits = ["apple", "banana", "mango"]
# while "apple" in fruits:
#     print("Apple found, removing...")
#     fruits.remove("apple")
# print(fruits)
#
#
# ✅ Runs until condition becomes false.
#
# 10. while with counter decrement
# count = 5
# while count > 0:
#     print(count)
#     count -= 1
#
#
# ✅ Loops in reverse.
#
# 11. while with multiple conditions
# x, y = 0, 5
# while x < 3 and y > 0:
#     print(f"x={x}, y={y}")
#     x += 1
#     y -= 1
#
#
# ✅ Loop runs until both conditions fail.
#
# 12. while with pass
# x = 0
# while x < 3:
#     pass   # placeholder (to implement later)
#     x += 1
#
#
# ✅ Used in framework stubs where logic is pending.
#
# 13. Chained condition in while
# x = 10
# while 5 < x < 15:
#     print(x)
#     x -= 2
#
#
# ✅ Uses chained comparison.
#
# 14. while with function return
# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1
#     else:
#         print("Blast off!")
#
# countdown(5)
#
# ⚡ Summary
#
# Basic while
#
# Infinite loop
#
# while + else
#
# break / continue
#
# Nested loops
#
# Simulating for
#
# With user input
# 
# With lists/dicts
#
# Counter increment/decrement
#
# Multiple conditions
#
# pass placeholder
#
# Chained conditions
#
# Inside functions
