#1.Elements
#Returns an iterator over elements, repeating each as many timesas its count
#Only positive counts are included
from collections import Counter
c = Counter(a=3,b=2,c=0,d=-1)
print(list(c.elements()))

#2.most_common([n])
#Returns the n most common elements and their counts as a list of tuples
#if n is omitted , returns all elements
c = Counter('abdksdhdwiaj')
print(c.most_common())
