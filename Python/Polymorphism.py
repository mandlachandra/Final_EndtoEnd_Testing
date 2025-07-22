#polymorphism means "one interface, many forms"
#The same method or operation can behave differently based on the object it is acting on.

#1.Method Overriding(RunTime Polymorphism)
#When a child class has a method with the same name as in the parent class, but different implementation

# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
#
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
#
# class Cat(Animal):
#     def speak(self):
#         print("cat meows")
#
# #same method call behaves differently
# for animal in [Dog(),Cat()]:
#     animal.speak()

#what are the types of polymorphism
#1.Compile-time(static) Achieved through method overloading (not directly supported in python)
#2.RunTime(dynamic) Achieved through method overriding.
#python supports dynamic polymorphism

#does python supports method overloading ?
#No, python doesnt support method overloading
#But we can achieve similar behaviour using default arguments or *args, **kwargs

def add(a,b,c=0):
    return a+b+c
print(add(2,3))
print(add(2,3,4))

#How is polymorphism implemented in python
#There are 2 ways
#1.Method Overriding(Inheritence)
#2.Duck Typing(object having required methods/attributes)

#what is method overriding ?
#When a child class provides its own implementation of a method already defined in the parent class

class parent:
    def show(self):
        print("parent")

class child(parent):
    def show(self):
        print("child")

obj = child()
obj.show()

#what is duck typing ?
