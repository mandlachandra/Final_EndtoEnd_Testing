#An iterator in python is an object that allows you to iterate(traverse) through all the elements of a collection
#(like list, tuple,strings) one at a time
#it implements 2 methods
#1.__iter__() - Returns the iterator object itself
#2.__next__() - Returns the next item, raises StopIteration when there are no more items

# my_list = [1, 2, 3]
#
# # Get iterator object
# it = iter(my_list)
#
# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3
# print(next(it))  # Raises StopIteration

class MyNumbers:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

numbers = MyNumbers(1, 5)
for num in numbers:
    print(num)
