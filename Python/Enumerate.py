#what is enumerate in python ?
# enumerate() is a built-in function in python
# It adds an index counter to an iterable(list,tuple,string etc) and returns an enumerate object
# By default indexing starts at 0, but you can specify a different start index

#Enumerate with list
fruits = ["apple","mangoes","banana","kiwi"]
for index , fruit in enumerate(fruits, start=1):
    print(index, fruit)

#Enumerate with string
word="python"

for index,char in enumerate(word,start=1):
    print(index,char)

#Enumerate with tuple
numbers = (10,20,30,40)

for i, num in enumerate(numbers):
    print(f"index {i}->value {num}")

#Enumerate with list comprehension
fruits = ["apple", "banana", "cherry"]
indexed = [(i,fruit) for i, fruit in enumerate(fruits)]
print(indexed)

#Convert Enumerate object to list/tuple
fruits1 = ["apple", "banana", "cherry","kiwi"]
enum_list = list(enumerate(fruits1))
print(enum_list)

enum_tuple = tuple(enumerate(fruits1,start=100))
print(enum_tuple)

#Enumerate with Dictionary (on keys or values)
data = {"a": 10, "b": 20, "c": 30}

#on keys
for i,key in enumerate(data):
    print(i,key)

#on values
for i,value in enumerate(data.values(),start=1):
    print(i,value)

#on items
for i,(k,v) in enumerate(data.items()):
    print(i,k,v)