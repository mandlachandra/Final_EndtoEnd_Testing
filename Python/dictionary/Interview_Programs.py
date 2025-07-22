#1.count frequency of each character in a string
s = "mandlachandrasekhar"
freq = {}

for char in s:
    if char in freq:
        freq[char] +=1

    else:
        freq[char] =1

print(freq)

#merge 2 dictionary
d1 = {"a":1,"b":3}
d2 = {"b":34,"c":45}

d1.update(d2)
print(d1)

#remove a key value pair
person = {"name":"sekhar","age":30}
removed_value = person.pop("age")
print("removed:",removed_value)
print("updated dict:",person)

#get all keys and values separately
d = {"x":10,"y":30}
print("keys:",list(d.keys()))
print("values:",list(d.values()))



