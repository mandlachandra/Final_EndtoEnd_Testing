#1. Sort a Dictionary by Keys (Ascending & Descending)
data ={'banana':3,'apple':4,'mango':1,'kiwi':2}

#ascending order by keys
sorted_by_keys = dict(sorted(data.items()))
print(sorted_by_keys)

#descending order
sorted_by_keys_desc = dict(sorted(data.items(),reverse=True))
print(sorted_by_keys_desc)


# 2. Sort a Dictionary by Values (Ascending & Descending)
data = {'banana': 3, 'apple': 5, 'mango': 2}

#ascending values
sorted_by_values = dict(sorted(data.items(),key=lambda item:item[1]))
print(sorted_by_values)

#descending values
sorted_by_values_desc = dict(sorted(data.items(),key=lambda item:item[1],reverse=True))
print(sorted_by_values_desc)

#Sort a Dictionary by Length of Key
data = {'kiwi': 2, 'strawberry': 7, 'apple': 3}
sorted_by_key_length = dict(sorted(data.items(),key=lambda item:len(item[0])))
print(sorted_by_key_length)

#Sort a List of Dictionaries by a Specific Key
fruits = [
    {'name':'banana','price':20},
    {'name':'apple','price':60},
    {'name':'kiwi','price':40}
]
sorted_fruits = sorted(fruits,key=lambda fruit:fruit['price'])
print(sorted_fruits)

#Sort a Nested Dictionary by Inner Dictionary Value
students={
    'john':{'math':87},
    'emma':{'math':78},
    'louis':{'math':96}
}
sorted_students = dict(sorted(students.items(),key=lambda item :item[1]['math']))#reverse=True))
print(sorted_students)

