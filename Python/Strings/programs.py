#what is string immutability in python
# Once a string is created it cannot be changed in place
# Any operation that appears to modify a string actually creates a new string object in memoryview

# s = "hello"
#
# print(id(s))
#
# s = s+"world" #looks like modification
# print(s)
# print(id(s)) #different address

#The memory address (id) changes proving a new object was created.

#why strings are immutable
# 1.Performance = Immutable objects can be cached and reused by python.
# 2.THread-safety = No worries about multiple threads chaning the same string in place
# 3.Hashability = Strings can be used as dictionary keys because thier hash values dont change

#How do you reverse words in strings
#using split() and join()
# sentence1 = "I love my county"
# words = sentence1.split()
# #print(words)
# reversed_words = words[::-1]
# result = ' '.join(reversed_words)
# print(result)
#
# #using reversed()
# sentence = "python is very easy"
# result = ' '.join(reversed(sentence.split()))
# print(result)

#how do you check if 2 strings are anagrams
#Two strings are anagrams if sorted characters match
#using sorted()
def is_anagram(str1,str2):
    str1 = str1.replace(" "," ").lower()
    str2 = str2.replace(" "," ").lower()
    return sorted(str1) == sorted(str2)

print(is_anagram("listen","silent"))

#what are the common string manipulation functions
# | Function        | Description                           | Example                                        |
# | --------------- | ------------------------------------- | ---------------------------------------------- |
# | `.lower()`      | Converts to lowercase                 | `"Hello".lower()` → `"hello"`                  |
# | `.upper()`      | Converts to uppercase                 | `"Hello".upper()` → `"HELLO"`                  |
# | `.capitalize()` | Capitalizes first letter              | `"hello world".capitalize()` → `"Hello world"` |
# | `.title()`      | Capitalizes first letter of each word | `"hello world".title()` → `"Hello World"`      |
# | `.swapcase()`   | Swaps upper ↔ lower case              | `"Hello".swapcase()` → `"hELLO"`               |


# | Function    | Description                       | Example                     |
# | ----------- | --------------------------------- | --------------------------- |
# | `.strip()`  | Removes leading & trailing spaces | `"  hi  ".strip()` → `"hi"` |
# | `.lstrip()` | Removes spaces from left          | `"  hi".lstrip()` → `"hi"`  |
# | `.rstrip()` | Removes spaces from right         | `"hi  ".rstrip()` → `"hi"`  |

# | Function     | Description                                 | Example                                |
# | ------------ | ------------------------------------------- | -------------------------------------- |
# | `.find()`    | Finds index of substring (first occurrence) | `"hello".find("l")` → `2`              |
# | `.rfind()`   | Finds index from right                      | `"hello".rfind("l")` → `3`             |
# | `.index()`   | Like `.find()` but errors if not found      | `"hello".index("e")` → `1`             |
# | `.replace()` | Replaces substring                          | `"hello".replace("l","x")` → `"hexxo"` |

# | Function               | Description             | Example                                 |
# | ---------------------- | ----------------------- | --------------------------------------- |
# | `.split()`             | Splits string into list | `"a,b,c".split(",")` → `['a','b','c']`  |
# | `.rsplit()`            | Splits from right       | `"a b c".rsplit(" ",1)` → `['a b','c']` |
# | `.splitlines()`        | Splits by line breaks   | `"a\nb".splitlines()` → `['a','b']`     |
# | `separator.join(list)` | Joins list into string  | `"-".join(['a','b'])` → `"a-b"`         |

# | Function        | Description            | Example                             |
# | --------------- | ---------------------- | ----------------------------------- |
# | `.startswith()` | Checks prefix          | `"hello".startswith("he")` → `True` |
# | `.endswith()`   | Checks suffix          | `"hello".endswith("lo")` → `True`   |
# | `.isalpha()`    | Only letters?          | `"abc".isalpha()` → `True`          |
# | `.isdigit()`    | Only digits?           | `"123".isdigit()` → `True`          |
# | `.isalnum()`    | Letters & digits only? | `"abc123".isalnum()` → `True`       |
# | `.isspace()`    | Only spaces?           | `"   ".isspace()` → `True`          |
# | `.islower()`    | All lowercase?         | `"abc".islower()` → `True`          |
# | `.isupper()`    | All uppercase?         | `"ABC".isupper()` → `True`          |
# | `.istitle()`    | Title case?            | `"Hello World".istitle()` → `True`  |

# | Function       | Description             | Example                                 |
# | -------------- | ----------------------- | --------------------------------------- |
# | `f""`          | f-strings for variables | `name="Bob"; f"Hi {name}"` → `"Hi Bob"` |
# | `.format()`    | Format values           | `"Hi {}".format("Bob")` → `"Hi Bob"`    |
# | `%` formatting | Old style               | `"Hi %s" % "Bob"` → `"Hi Bob"`          |

