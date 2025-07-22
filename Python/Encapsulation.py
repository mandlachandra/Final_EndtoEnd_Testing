#Encapsulation is a principle of oops where we restrict direct access to an objects data(attributes) and exposes it only through methods
#Think of it as hiding sensitive data

#Wrapping data(variables) and methods(functions) together into a single unit(class) and restricting direct access to some of the objects.


#how is Encapsulation achieved in python
#by making attributes private using underscores
#_protected_var
#__privates__
#by providing getter and setter methods to access or modify private data

class BankAccount:

    def __init__(self,account_number,balance):
        self.account_number = account_number #public
        self._balance = balance #protected
        self.__pin = 1234  #private

    def display_balance(self,pin):
        if pin == self.__pin:
            print(f"Account Balance: {self._balance}")
        else:
            print("Invalid pin!")

    def deposit(self,amount):
        if amount>0:
            self._balance +=amount
            print(f"Deposited {amount},New balance: {self._balance}")
        else:
            print("Invalid amount")

    def __update_pin(self,new_pin):  #private method
        self.__pin = new_pin
        print("Pin updated successfully")

acc = BankAccount("123456",6000)

#public variable
print(acc.account_number) #allowed

#protected variables (allowed but discouraged)
print(acc._balance)

#private variable (not directly accessed)
# print(acc.__pin)