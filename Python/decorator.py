#Decorator is a function that takes another function as input , adds some functionality to it, returns a new function
#without modifying the original functions code
import pytest


#They are widely used in logging,authentication ,timing functions etc

# def decorator_function(original_function):
#     def wrapper_function():
#         # Code to execute **before** original function
#         print("Before the original function")
#
#         # Call the original function
#         original_function()
#
#         # Code to execute **after** original function
#         print("After the original function")
#
#     return wrapper_function

# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper
#
# @my_decorator  # This is equivalent to say_hello = my_decorator(say_hello)
# def say_hello():
#     print("Hello!")
#
# say_hello()
# Q1. What is a decorator in Python? Why do we use it?
# ✅ Answer:
# A decorator is a function in Python that takes another function (or class) as an argument, adds some functionality to it, and returns a new function. It is commonly used to modify or extend the behavior of functions or methods without changing their code.
#
# Why use it?
#
# Code reusability.
#
# Clean and maintainable code.
#
# Dynamically add functionality.

# Q2. Write a simple example of a decorator.
# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()

#can a decorator accept arguments ?show with an example
#yes a decorator can accept arguments by creating a decorator factory

def repeat(num_times):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"hello, {name}")

greet("chandra")

#what is the difff b/w function decorator and class decorator ?
#function decorator applies to function or methods
#the purpose is to modify or extend behaviour of functions
#@staticmethod, @classmethod

#applied to classes
#the purpose is to modify or extend behaviour of classes
#@dataclass,@singleton

#how are decorators used in python libraries (real time examples)
#@static method - marks a method as static
#@class method - passes the class as the first argument instead of self
#@propert - converts a method to a read only property

@pytest.Mark.skip(reason="Not implemented yet")
def test_feature():
    pass

#Can decorators be applied to classes? Show with an example.
#yes decorators can also modify classes
def uppercase_class(cls):
    cls.name = cls.name.upper()
    return cls

@uppercase_class
class Person:
    name = "Sekhar"

print(Person.name)

#How would you write a decorator that caches the result of a function (memoization)?

# def memoize(func):
#     cache = {}
#     def wrapper(n):
#         if n not in cache:
#             cache[n] = func(n)
#         return cache[n]
#     return wrapper
#
# @memoize
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)
#
# print(fib(10))  # Output: 55

# Q8. What happens when you apply @staticmethod, @classmethod, and @property?
# @staticmethod: Defines a method that does not depend on instance or class (no self or cls).
#
# @classmethod: Receives the class (cls) as the first parameter.
#
# @property: Allows you to access a method like an attribute.

# Q7. Can you chain multiple decorators? Show with an example.
# ✅ Answer:
# Yes, you can stack multiple decorators.
# def decorator1(func):
#     def wrapper():
#         print("Decorator 1")
#         func()
#     return wrapper
#
# def decorator2(func):
#     def wrapper():
#         print("Decorator 2")
#         func()
#     return wrapper
#
# @decorator1
# @decorator2
# def say_hello():
#     print("Hello!")
#
# say_hello()
#
# Q5. Can you write a decorator that logs the execution time of a function?
# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} executed in {end - start:.4f} seconds")
#         return result
#     return wrapper
#
# @timer
# def slow_function():
#     time.sleep(2)
#     print("Function complete!")
#
# slow_function()



