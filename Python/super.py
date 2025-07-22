#super() is a built in function in python used to call methods or constructors of a parent(super) class

#it is commonly used in inheritence when you want a child class to access or extend the behaviour  of its own class.

#why use super()
#To reuse parent class code without  hardcoding the parents name
#To avoid duplication when overriding methods
#to make your code easy to maintain

#syntax
#super().method_name(args)

#or in constructor
#super().__init__(args)

#using super() in constructor
class parent:

    def __init__(self,name):
        print("parent constructor")
        self.name = name

class child(parent):
    def __init__(self,name,age):
        print("child constructor")
        super().__init__(name)
        self.age = age

c = child("Alice",40)
print(c.name, c.age)

#using super() to call parent class

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        super().show()  # 👈 Call Parent show()
        print("This is Child class")

c = Child()
c.show()



