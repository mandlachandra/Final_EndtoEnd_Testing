#Nested list
def flatten_list(nested_list):
    flat = []

    for item in nested_list:
        if isinstance(item,list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)

    return flat

input_data = [3, 5, [9, [7, 8, [12, 71]]]]
output = flatten_list(input_data)
print("The output is:",output)

from collections import Counter
str = "secondmostfrequencycharacter"
freq = Counter(str)


#get all characters sorted by frequency
sorted_freq = freq.most_common()
print("frequencies:",sorted_freq)

#get 2nd most frequency


