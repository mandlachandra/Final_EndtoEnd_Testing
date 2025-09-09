#What is the difference between is and == in Python?
# == compares values of 2 objects
# Returns True if the contents are the same
# a= [1,2,3]
# b =[1,2,3]
# print(a=b)  #True

# is compares memory address of 2 objects
# Returns True if both variables point to the same object in memory
# c = a
# print(c is a) #True

#
# #implement a string matcher using regex to validate email and phone numbers
import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
    return re.match(email_regex,email) is not None

def is_valid_phone(phone):
    phone_regex=r'^(\+91[\-\s]?|0)?[6-9]\d{9}$'
    return re.match(phone_regex,phone) is not None

emails = [
    "test@gmail.com",
    "user.name#domian.com",
    "bad-email@com",
    "user@domain"
]
phones = [
    "9837272812",
    "+91=9282873780",
    "09282883833",
    "938snsj93k"
]
print("email validation results:")
for email in emails:
    print(f"{email}:{is_valid_email(email)}")

print("\n phone validation results:")
for phone in phones:
    print(f"{phone}:{is_valid_phone(phone)}")

#write code to count the frequency of characters in a string using lambda
from functools import reduce

def char_frequency(s):
    return reduce(lambda acc, c: {**acc,c:acc.get(c,0)+1},s,{})

string = "programming"
freq= char_frequency(string)
print(freq)

#write a class with private, protected and public members and demonstrate access
class DemoClass:

    def __init__(self):
        self.public_var = "i am public"
        self._protected_var = "i am protected"
        self.__private_var = "i am private"

    def public_method(self):
        print("Public method")
        print(self.public_var)
        print(self.__private_var)
        print(self._protected_var)

    def _protected_method(self):
        print("protected method")

    def __private_method(self):
        print("private method")

    #Access private method inside class
    def access_private_method(self):
        self.__private_method()

    #subclass to demonstrate inheritence
class SubClass(DemoClass):
    def __init__(self):
        super().__init__()

    def access_private_method(self):
        print("Accessing from subclass")
        print("public:",self.public_var)
        print("protected:",self._protected_var)

obj = DemoClass()
print("Access from outside class")
print(obj.public_var)





