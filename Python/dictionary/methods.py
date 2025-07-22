#dictionary in python is an unordered,mutable and key-value pair data structure
#methods
#1.clear()
d = {"a":1,"b":2}
d.clear()
print(d)

#2.copy()
d1 = {"a":10,"b":20}
copy_d = d1.copy()
print(copy_d)

#3.fromkeys()
#creates a new dictionary from given sequence of keys with a common value
keys = ["a","b","c"]
d3 = dict.fromkeys(keys,0)
print(d3)

#4.get()
#returns the value for a key if present, else returns None (or a default value)

d4 = {"a":11,"b":3}
print(d4.get("a"))
print(d4.get("z",0))

#items()
#returns a view object of key-value pairs
d5 = {"a":21,"b":32}
print(d5.items())

#keys()
d6 = {"a":101,"b":202}
print(d6.keys())

#values()
d7 = {"a":12,"b":32}
print(d7.values)

#pop()
d8 = {"a":1,"b":2}
value = d8.pop("a")
print(value)
print(d8)

#popitem()
d9 = {"a": 1, "b": 2}
item = d9.popitem()
print(item)  # ('b', 2)
print(d9)     # {'a': 1}

#setdefault
d10 = {"a": 1}
print(d10.setdefault("a", 100))  # 1
print(d10.setdefault("b", 200))  # 200
print(d10)

#update()
d11 = {"a": 1, "b": 2}
d11.update({"b": 3, "c": 4})
print(d11)

