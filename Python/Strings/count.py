#1.count occurrence of a character in s string
s = "banana"
print(s.count("a"))

#2.count occurrence of a substring
s1 = "banana"
print(s1.count("ana"))

#3.count of occurrence of each character in a string
from collections import Counter
s2 = "mandlachandrasekhar"
count = Counter(s2)
print(count)

#count no of words in a string
s3 = "hello world in python program"
print(len(s3.split()))

#count vowels and constants
s4 = "welcome"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in s4 if char in vowels)
constants_count = sum(1 for char in s4 if char.isalpha() and char not in vowels )

print("Vowels:",vowel_count)
print("constants:",constants_count)

#count uppercase and lowercase letters
s5 = "Helloworld123"
upper = sum(1 for char in s5 if char.isupper())
lower = sum(1 for char in s5 if char.islower())

print("uppercase:",upper)
print("lowercase:",lower)

#count digits, letters and special characters
s6 = "Hello123#@!"
letters = sum(1 for c in s6 if c.isalpha())
digits = sum(1 for c in s6 if c.isdigit())
special = len(s6) - letters - digits
print("letters:",letters)
print("digist:",digits)
print("special characters:",special)

#count duplicate characters
from collections import Counter

s7 = "programming"
duplicates = {k:v for k, v in Counter(s7).items() if v>1}
print(duplicates)

#count words starting with a specific letter
s8 = "apple banana apricot kiwi"
count = sum(1 for word in s8.split() if word.startswith("a"))
print(count)