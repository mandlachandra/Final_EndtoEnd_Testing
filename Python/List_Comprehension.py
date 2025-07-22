#List comprehension is a short and elegant way to create a new list by applying an opertionto each item in an existing list
#it is basically one liner for loops

#[expression for item in iterable if condition]
#1.Squares of numbers
nums = [1,2,3,4]
squares = [x**2 for x in nums]
print(squares)

#2.filter even numbers
nums1 = [1,2,3,4,5,6]
even_numbers = [x for x in nums1 if x%2==0]
print(even_numbers)

#3.convert to uppercase
fruits = ["apple","mango","banana"]
upper = [fruit.upper() for fruit in fruits]
print(upper)

#4.Nested loops
#create pairs (x,y) where x from(1,2) from (3,4)
pairs = [(x,y) for x in [1,2] for y in (3,4)]
print(pairs)

#5.If -else
numss =[1,2,3,4,5,6]
labels = ['even' if x%2==0 else 'odd' for x in numss]
print(labels)

#6.Flatten list
nested = [[1,2],[3,4]]
flat = [num for sublist in nested for num in sublist]
print(flat)