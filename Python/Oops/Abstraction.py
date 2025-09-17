 #Abstraction means hiding the implementation details and showing only the essential features of an object
# #In python Abstraction is achived by using
# #Abstract Base Class(ABC)
# #@abstractmethod decorator
#
# # from abc import ABC,abstractmethod
#
# #create an Abstract Base Class
# #An Abstract class can have:
# #Abstract methods (no implementation)
# #concrete methods (with implementation)
#
# from abc import ABC, abstractmethod
#
# #Abstract Class
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# #concrete class
# class Car(Vehicle):
#     def start(self):
#         print("car engine started.")
#
#     def stop(self):
#         print("car engine stopped.")
#
# class Bike(Vehicle):
#     def start(self):
#         print("Bike engine started")
#
#     def stop(self):
#         print("Bike engine stopped.")
#
#
# car = Car()
# car.start()
# car.stop()
#
# bike = Bike()
# bike.start()
# bike.stop()
#
# #you cannot instantiate an abstract class directly
# #All child classes must implement all abstract class
#
#
# from abc import ABC, abstractmethod
#
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#
# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Credit Card.")
#
# class PayPalPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using PayPal.")
#
# # Using the classes
# payment1 = CreditCardPayment()
# payment1.pay(5000)
#
# payment2 = PayPalPayment()
# payment2.pay(3000)
#
# #what is abstraction in python ?how it is achieved ?
# # Abstraction is a concept where we hide the implementation details and only expose the functionality to the user.
# #
# # In Python, abstraction is achieved using:
# #
# # Abstract classes (using abc.ABC)
# #
# # Abstract methods (using @abstractmethod)
# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#
# #Here Vehicle is an abstract class and start is an abstract method
#
# #2.why do we need abstraction in python ?
# #to hide complex internal details
# #provide a clear interface for users
#
# #can an abstract class have concrete methods in python ?
# #yes abstract class can have concrete (non-abstract) methods
# #abstract classes can mix both abstract and concrete methods
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
#     def sleep(self): #concrete method
#         print("sleeping")
#
# #child class must override abstract methods but can reuse concrete methods
#
# #what happens if a child class does not implement all abstract methods ?
# #if a child class doesn't override all abstract methods, it itself becomes abstract
#
# #How is abstraction implemented in pythons standard library ?
# #in selenium Webdriver is an abstract class and classes like chrome,firefox implement its abstract methods(get(),quit())
#
# #Abstract Class = Abstract + concrete methods
# #Interface in python = Only abstract methods
#
# #can you give a real time example of abstraction
# #In a banking system you have a base class payment
# # class Payment(ABC):
# #     @abstractmethod
# #     def pay(self,amount):
# #         pass
# #child classes like CreditCardPayment , UPI Payment etc implement pay() differently
# #The users calls pay() without knowing how each method works internally.
#
# #Is it mandatory to use @abstractmethod in abstract classes ?
# #NO
# #you can create an abstract class without abstract methods
# #Then it acts like a regular class unless you can use @abstractmethod to enforce implementation

#Instead of repeating open_page() , get_title(),click_element() you can define abstract page class

from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By

class BasePage(ABC):

    def __init__(self,driver):
        self.driver = driver

    @abstractmethod
    def open_page(self,url):
        pass

    @abstractmethod
    def get_title(self):
        pass

class HomePage(BasePage):

    def open_page(self,url = "https://michaels.com"):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title