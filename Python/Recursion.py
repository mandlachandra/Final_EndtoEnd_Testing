#Factorial using recursion
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num = 5
# result = factorial(num)
# print(f"factorial of {num} is {result}")

#fibonacci using recursion
# def fibonacci(n):
#     if n ==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# terms= 7
# print(f"fibonacci sequence up to {terms} terms:")
# for i in range(terms):
#     print(fibonacci(i),end = " ")

#sum of digits using recursion
# def sum_of_digits(n):
#
#     if n == 0:
#         return 0
#
#     return (n%10)+sum_of_digits(n//10)
#
# number = 12345
# result = sum_of_digits(number)
# print(f"sum of digits of {number} is {result}")

#reverse a string using recursion

def reverse_string(s):

    if len(s)<=1:
        return s

    return reverse_string(s[1:]) + s[0]

text = "hello"
result = reverse_string(text)
print(f"reversed string: {result}")



