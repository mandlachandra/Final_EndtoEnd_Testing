#Q1. Why are strings immutable in Python?
#Strings are immutable because once created their memory cannot be modified
#Any operations like concatenation or slicing creates a new string object
s = "hello"
print(id(s))
s+="world"
print(id(s)) #new memory location

#Q2. Reverse a string without using slicing.
s = "python"
rev = ''.join(reversed(s))
print(rev)

#Q3. Count occurrences of each character in "mississippi".
s = "mississippi"
count = {ch: s.count(ch) for ch in set(s)}
print(count)
from collections import Counter
freq = Counter(s)
print(freq)

#Q4. Extract the domain from an email string "test@gmail.com".
email = "test@gmail.com"
domain = email.split("@")[1]
print(domain)