import re

input_str = "Test12QA 34abc 56 rst abc12"

# 1. Sum of Digits
digits = [int(ch) for ch in input_str if ch.isdigit()]
sum_digits = sum(digits)

# 2. Print String removing digits and spaces
string_only = re.sub(r"[0-9 ]", "", input_str)

# 3. Order the Digits in Ascending
digits_sorted = sorted(digits)

# 4. Second Largest Number
unique_digits = sorted(set(digits))
second_largest = unique_digits[-2] if len(unique_digits) >= 2 else None

# 5. Positions of Second Largest number
positions = [i for i, ch in enumerate(input_str) if ch.isdigit() and int(ch) == second_largest]

# Print outputs
print("1. Sum of Digits:", sum_digits)
print("2. String without digits & spaces:", string_only)
print("3. Digits Ascending:", digits_sorted)
print("4. Second Largest Digit:", second_largest)
print("5. Positions of Second Largest Digit:", positions)
