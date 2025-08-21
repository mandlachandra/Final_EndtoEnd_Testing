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

#2nd most character
str = "secondmostfrequentcharacter"

from collections import Counter

#Count frequency of each character
freq = Counter(str)

#get all characters sorted by frequency
sorted_freq=freq.most_common()

#print sorted frequencies
print("frequencies:",sorted_freq)

#get 2nd most freq
if len(sorted_freq) >=2:
    second_most_character, second_most_count = sorted_freq[1]
    print(f"2nd most character: '{second_most_character}' with count {second_most_count}")
else:
    print("Not enough unique characters to find 2nd most character")

#shallow copy =Shallow copy creates a new object but does not create copies of nested objects
# import copy
#
# original = [[1,2,3],[4,5,6]]
# shallow = copy.copy(original)
#
# original[0][0] = 99
# print(shallow[0][0])  # Output: 99 (because inner list is shared)



import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original) #deep copy will create completely independent object including all nested objects.
original[0][0] =99
print(deep[0][0])



