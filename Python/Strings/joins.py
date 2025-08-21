#Join a list of strings with a space
words = ["welcome","to","india"]
result = " ".join(words)
print(result)

#join a list with a custom saperator
date_parts = ["2025","07","16"]
result1 = "-".join(date_parts)
print(result1)

#join characters in a string with a space
s = "hello"
result2 = " ".join(s)
print(result2)

#join list of integers into a string
nums = [1,2,3]
result = "-".join(str(n) for n in nums)
print(result)

