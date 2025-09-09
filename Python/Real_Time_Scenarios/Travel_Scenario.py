# from abc import ABC, abstractmethod
#
# #Abstraction
# class Journey(ABC):
#
#     @abstractmethod
#     def travel(self):
#         pass
#     @abstractmethod
#     def show_expenses(self):
#         pass
#
# #Encapsulation
# class Trip(Journey):
#
#     def __init__(self,start,destination):
#         self.__start = start
#         self.__destination = destination
#         self.stop = [] #list to hold stops
#         self.expenses = {} #dictionary to hold food expenses
#         print(f"Trip started from {self.__start} to {self.__destination}")
#
#     #instance method
#     def add_stop(self,stop,amount):
#
from abc import ABC, abstractmethod

# 🔹 Abstraction
class Journey(ABC):
    @abstractmethod
    def travel(self):
        pass

    @abstractmethod
    def show_expenses(self):
        pass


# 🔹 Encapsulation
class Trip(Journey):
    def __init__(self, start, destination):
        self.__start = start          # private attribute
        self.__destination = destination
        self.stops = []               # list to hold stops
        self.expenses = {}            # dictionary to hold food expenses
        print(f"🚉 Trip started from {self.__start} to {self.__destination}")

    # instance method
    def add_stop(self, stop, amount):
        self.stops.append(stop)
        self.expenses[stop] = amount
        print(f"✅ Added stop {stop} with expense ₹{amount}")

    # polymorphism (overriding abstract method)
    def travel(self):
        print("🛤️ Traveling through stops...")
        for stop in self.stops:
            print(f"Reached {stop}, spent ₹{self.expenses[stop]} on food")

    # polymorphism (overriding abstract method)
    def show_expenses(self):
        total = sum(self.expenses.values())
        print("\n📊 Expense Report:")
        for stop, amt in self.expenses.items():
            print(f"{stop}: ₹{amt}")
        print(f"Total Trip Expense: ₹{total}")
        return total

    # class method
    @classmethod
    def trip_type(cls):
        return "This is a Train Journey 🚂"

    # static method
    @staticmethod
    def welcome_message():
        print("🙌 Welcome to Indian Railways Travel System")

    # Destructor
    def __del__(self):
        print("🛑 Trip object deleted. Journey completed!")


# 🔹 Inheritance
class LuxuryTrip(Trip):
    def __init__(self, start, destination, luxury_tax):
        super().__init__(start, destination)
        self.luxury_tax = luxury_tax

    # method overriding (Polymorphism)
    def show_expenses(self):
        total = super().show_expenses()
        total_with_tax = total + self.luxury_tax
        print(f"Luxury Tax Applied: ₹{self.luxury_tax}")
        print(f"Final Total Expense: ₹{total_with_tax}")
        return total_with_tax


# ------------------ Driver Code ------------------

# static method
Trip.welcome_message()

# class method
print(Trip.trip_type())

# Creating Trip Object
my_trip = LuxuryTrip("Andhra Pradesh", "Delhi", luxury_tax=500)

# Adding Stops and Expenses
my_trip.add_stop("Bangalore", 1000)
my_trip.add_stop("Nagpur", 1000)
my_trip.add_stop("Rajasthan", 1000)
my_trip.add_stop("Jaipur", 1000)
my_trip.add_stop("Delhi", 1000)

# Travel
my_trip.travel()

# Show Expenses
my_trip.show_expenses()
