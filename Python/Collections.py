# str = "secondmostfrequentcharacter"
#
# from collections import Counter
#
# #Count frequency of each character
# freq = Counter(str)
#
# #get all characters sorted by frequency
# sorted_freq=freq.most_common()
#
# #print sorted frequencies
# print("frequencies:",sorted_freq)
#
# #get 2nd most freq
# if len(sorted_freq) >=2:
#     second_most_character, second_most_count = sorted_freq[1]
#     print(f"2nd most character: '{second_most_character}' with count {second_most_count}")
# else:
#     print("Not enough unique characters to find 2nd most character")

#The collection module provides high-performance container datatypes and alternatives to pythons general purpose built in containers
#1.Counter = count occurence of elements
from collections import Counter

#count characters
c = Counter("banana")
print(c)

#most common elements
print(c.most_common(2))

#use case : words count ,frequency analysis