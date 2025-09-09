


#
# #extract only numbers
# numbers = re.findall(r'\d+',url)
#
# #combine in one string
# only_numbers = ''.join(numbers)
# print("Extracted numbers:",only_numbers)
#
# #extract only upper case
# uppercase_letter = re.findall(r'[A-Z]',url)
#
# #join and print
# result = ''.join(uppercase_letter)
# print(result)
#
# #extract only lower case
# lowercase_letter = re.findall(r'[a-z]',url)
#
# #join
# output = ''.join(lowercase_letter)
# print(output)

# import re
#
# # Find all uppercase letters
# print("Uppercase letters:", re.findall(r'[A-Z]', url))
#
# # Find all digits
# print("All numbers:", re.findall(r'\d+', url))
#
# # Find all lowercase letters
# print("Lowercase letters:", re.findall(r'[a-z]', url))
#
# # Find all special characters (non-alphanumeric)
# print("Special characters:", re.findall(r'[^a-zA-Z0-9]', url))
#
# # Find all words
# print("Words:", re.findall(r'\w+', url))
#
# match = re.search(r'meeting_\w+', url)
# if match:
#     print("Meeting pattern found:", match.group())
#
# match = re.match(r'https', url)
# if match:
#     print("Starts with 'https':", match.group())
#
# # Replace all digits with '*'
# print("Digits replaced:", re.sub(r'\d', '*', url))
#
# # Remove special characters
# print("Only alphanumerics:", re.sub(r'[^a-zA-Z0-9]', '', url))
#
# # Split by special characters
# print("Split by non-alphanum:", re.split(r'[^a-zA-Z0-9]', url))
#
# # Split by '&' (common URL param delimiter)
# print("Split by '&':", re.split(r'&', url))
#
# pattern = re.compile(r'[A-Z]+')
# print("Compiled pattern result:", pattern.findall(url))
#
# for match in re.finditer(r'\d+', url):
#     print("Number found:", match.group(), "at position:", match.span())

import re

#match
result = re.match(r"hello",'hello world')
print(result.group())

#search
result = re.search(r"love","i am indian and i love my country")
print(result.group())

#fullmatch
result = re.fullmatch(r"\d{4}","1234")
print(result.group())

#findall
result = re.findall(r"\d","my number is 12345")
print(result)

#finditer
result = re.finditer(r"\d","123abc45")
for match in result:
    print(match.group(),"at index",match.start())

#split
result = re.split(r"\s","python is great")

#subn
result = re.subn(r"\d","#","user1234")
print(result)
print(result)

#sub
result = re.sub(r"\d","#","User123")
print(result)

#subn
result = re.subn(r"\d","#","user1234")
print(result)