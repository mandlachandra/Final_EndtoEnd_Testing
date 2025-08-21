from abc import ABC ,abstractmethod

#abstraction
class Account(ABC):

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

#Encapsulation + Inheritence
class BankAccount(Account):
    def __init__(self,account_number,initial_balance=0):
        self._account_number = account_number
        self.__balance = initial_balance #Encapsulated

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if 0 < amount <=self.__balance:
            self.__balance -=amount
            print(f"withdraw: {amount}")

        else:
            print("Invalid or insufficient funds")


#Inheritence+Polymorphism
class SavingsAccount(BankAccount):
    def withdraw(self,amount):
        print("[Savings Account withdraw]")
        super().withdraw(amount)

class CurrentAccount(BankAccount):
    def withdraw(self,amount):
        print("[Current Account Withdraw]")
        super().withdraw(amount)

#class/object
class Customer:

    def __init__(self,name,account):
        self.name = name
        self.account = account


    def show_balance(self):
        print(f"{self.name}'s balance: {self.account.get_balance()}")

#create instances(objects)
savings = SavingsAccount("CHANDRA",2000)
current = CurrentAccount("mandla",4000)

cust1 = Customer("max",savings)
cust2 = Customer("joe",current)

#Inherit
cust1.show_balance()
cust1.account.deposit(1000)
cust1.account.withdraw(300)
cust1.show_balance()

print("...............")

cust2.show_balance()
cust2.account.deposit(1000)
cust2.account.withdraw(3000)  # should show insufficient
cust2.show_balance()
