# 1. Basic Example
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
#
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
#
# # Using abstraction
# animals = [Dog(), Cat()]
# for a in animals:
#     print(a.sound())
#
#
# ✅ Output:
#
# Bark
# Meow
#
#
# 👉 We don’t care how Dog or Cat makes sound, only what sound method returns.
#
# 2. With Constructor & Concrete Methods
# from abc import ABC, abstractmethod
#
# class Bank(ABC):
#     def __init__(self, balance):
#         self.balance = balance
#
#     @abstractmethod
#     def interest_rate(self):
#         pass
#
#     def show_balance(self):
#         return f"Balance: {self.balance}"
#
# class SBI(Bank):
#     def interest_rate(self):
#         return "Interest Rate: 5%"
#
# class HDFC(Bank):
#     def interest_rate(self):
#         return "Interest Rate: 6%"
#
# banks = [SBI(10000), HDFC(20000)]
# for b in banks:
#     print(b.show_balance(), "|", b.interest_rate())
#
#
# ✅ Abstract + Normal methods together.
#
# 3. Abstraction in Real Projects (Automation Example)
#
# Suppose you are testing different browsers in Selenium:
#
# from abc import ABC, abstractmethod
#
# class Browser(ABC):
#     @abstractmethod
#     def open_browser(self):
#         pass
#
#     @abstractmethod
#     def close_browser(self):
#         pass
#
# class Chrome(Browser):
#     def open_browser(self):
#         return "Chrome Browser Opened"
#
#     def close_browser(self):
#         return "Chrome Browser Closed"
#
# class Firefox(Browser):
#     def open_browser(self):
#         return "Firefox Browser Opened"
#
#     def close_browser(self):
#         return "Firefox Browser Closed"
#
# # Example usage
# browsers = [Chrome(), Firefox()]
# for b in browsers:
#     print(b.open_browser(), "|", b.close_browser())
#
#
# ✅ You write common methods in abstract class but implement differently for each browser.
#
# 4. Abstraction with Multiple Abstract Methods
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
# c = Circle(5)
# print("Area:", c.area(), "Perimeter:", c.perimeter())
#
# 5. Partial Abstraction (mix of abstract + concrete methods)
# from abc import ABC, abstractmethod
#
# class Payment(ABC):
#     @abstractmethod
#     def make_payment(self, amount):
#         pass
#
#     def receipt(self, amount):
#         return f"Payment of {amount} successful!"
#
# class CreditCard(Payment):
#     def make_payment(self, amount):
#         return f"Paid {amount} using Credit Card"
#
# c = CreditCard()
# print(c.make_payment(500))
# print(c.receipt(500))
#
#
# ✅ Concrete method (receipt) reused across all child classes.
#
# 6. Interfaces using Abstraction
#
# Python doesn’t have interfaces like Java, but you can mimic using abstract classes.
#
# from abc import ABC, abstractmethod
#
# class Database(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
# class MySQL(Database):
#     def connect(self):
#         return "Connected to MySQL"
#
#     def disconnect(self):
#         return "Disconnected from MySQL"
#
# class PostgreSQL(Database):
#     def connect(self):
#         return "Connected to PostgreSQL"
#
#     def disconnect(self):
#         return "Disconnected from PostgreSQL"
#
# dbs = [MySQL(), PostgreSQL()]
# for db in dbs:
#     print(db.connect(), "|", db.disconnect())
#
#
# 👉 Abstract class works like an interface here.
#
# 7. Multiple Inheritance with Abstraction
# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def method_a(self):
#         pass
#
# class B(ABC):
#     @abstractmethod
#     def method_b(self):
#         pass
#
# class C(A, B):
#     def method_a(self):
#         return "Method A implemented"
#
#     def method_b(self):
#         return "Method B implemented"
#
# c = C()
# print(c.method_a(), "|", c.method_b())
#
#
# ✅ Abstraction works even with multiple inheritance.
#
# 🔹 Why Use Abstraction?
#
# ✅ Hides implementation, exposes only functionality
# ✅ Improves code reusability and readability
# ✅ Helps achieve loose coupling (decouples “what” from “how”)
# ✅ Enforces method implementation in child classes