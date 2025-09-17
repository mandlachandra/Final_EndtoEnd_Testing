#compress string
#reverse a string
# str = "mandla chandra sekhar"
# print(str[::-1])
#
# str1 = "chandra"
# rev_s = ''.join(reversed(str1))
# print(rev_s)
#
# str2 = "i love my india"
# result = ''
# for c in str2:
#     result = c + result
# print(result)

#check if palindrome
# def is_palindrome(s):
#     return s == s[::-1]
#
# print(is_palindrome("madam"))
# print(is_palindrome("leaf"))
#
# #count vowels and constants
# def count_vowels_constants(s):
#     vowels = "aeiou"
#     vowels_count =0
#     constants_count =0
#
#     for ch in s:
#         if ch in vowels:
#             vowels_count +=1
#         else:
#             constants_count+=1
#
#     return vowels_count,constants_count
# s ="i love my india"
# v,c = count_vowels_constants(s)
# print(f"vowels: {v} and constant: {c}")
#
# #remove duplicates
# def remove_duplicates(s):
#     result = ""
#     for ch in s:
#         if ch not in result:
#             result +=ch
#     return result
# print(remove_duplicates("mandlachandra"))
#
# #capitalize first character of each word
# ss = "mandla chandra sekhar"
# result = ss.title()
# print(result)

#compress a string
# def compress_string(s):
#     result = ""
#     count=1
#
#     for i in range(1,len(s)):
#         if s[i] == s[i-1]:
#             count+=1
#         else:
#             result +=str(count) + s[i-1]
#             count =1
#     result+=str(count)+s[-1]
#     return result
#
# print(compress_string("aaaaaaabbbbbccccdddd"))
#
# #count of occurrence of a character in string
# s = "banana"
# print(s.count("a"))
#
# #count occurrence of a substring
# s1 = "banana"
# print(s.count("ana"))
#
# #count occurrence of each character in a string
# from collections import Counter
# str = "mandlachandra"
# freq_char = Counter(str)
# print(freq_char)

#count occurrence of each word in a string
from collections import Counter
str = "mandla chandra sekhar loves india a lot loves"
words = str.split()
freq_words = Counter(words)
print(freq_words)

#count number of words in a string
str = "mandla chandra sekhar is as was to me"
print(len(str.split()))

#count uppercase and lowercase
s4 = "HelloWorldFromIndia"
upper = sum(1 for char in s4 if char.isupper())
lower = sum(1 for char in s4 if char.islower())
print("is upper:",upper)
print("is lower:", lower)

#count digits,numbers and special characters
s6 = "Hello123#@!"
letters = sum(1 for char in s6 if char.isalpha())
numbers = sum(1 for char in s6 if char.isdigit())
special = len(s6)-letters-numbers
print("letters:",letters)
print("digits:",numbers)
print("special:",special)

#count words staring with special letter
s8 = "apple banana apricot kiwi"
count = sum(1 for word in s8.split() if word.startswith("a"))
print(count)

#count frequency of each character in a string
str = "mandlachandrasekhar"
freq = {}

for char in str:
    if char in freq:
        freq[char] += 1

    else:
        freq[char] = 1

print(freq)

#join a list os strings with space
words = ["welcome","to","india"]
result = ''.join(words)
print(result)

#join list of intergers into string
nums = [1,2,3,4,5,6]
result = '-'.join(str(n) for n in nums)
print(result)
#............................
#List
#How do you remove duplicates from list
#1.using set
# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# unique_fruits = list(set(fruits))
# print(unique_fruits)

#2.using dict.fromkeys()
# fruits = ["apple", "banana", "apple", "cherry", "banana"]
# unique_fruits = list(dict.fromkeys(fruits))
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
# nums = [x for x in nums if x!=2]
# print(nums)

#find common elements in 2 list
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_elements = list(set(list1) & set(list2))
# print(common_elements)
