#Decorato is a function that takes another function as input , adds some functionality to it, returns a new function
#without modifying the original functions code

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

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator  # This is equivalent to say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()
