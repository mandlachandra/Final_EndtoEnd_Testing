# class BankAccount:
#     def __init__(self, account_number, pin, balance=0):
#         self.account_number = account_number
#         self.__pin = pin         # private for security
#         self.balance = balance
#
#     def check_balance(self, pin):
#         if pin == self.__pin:
#             return self.balance
#         else:
#             raise ValueError("Invalid PIN. Access Denied!")
#
#     def deposit(self, amount, pin):
#         if pin != self.__pin:
#             raise ValueError("Invalid PIN. Transaction Failed!")
#         if amount <= 0:
#             raise ValueError("Deposit amount must be greater than 0.")
#         self.balance += amount
#         return self.balance
#
#     def update_pin(self, old_pin, new_pin):
#         if old_pin != self.__pin:
#             raise ValueError("Incorrect old PIN. Cannot update.")
#         self.__pin = new_pin
#         return True
#
#
# # --- Example Usage + Assertions (like test cases) ---
# account = BankAccount(account_number=12345, pin=1111, balance=5000)
#
# # ✅ Check balance
# assert account.check_balance(1111) == 5000
#
# # ✅ Deposit amount
# assert account.deposit(2000, 1111) == 7000
#
# # ✅ Update PIN
# assert account.update_pin(1111, 2222) == True
#
# # ✅ Balance check with new PIN
# assert account.check_balance(2222) == 7000
#
# # ❌ Wrong PIN should raise error
# try:
#     account.check_balance(1234)
# except ValueError as e:
#     assert str(e) == "Invalid PIN. Access Denied!"
#
# # ❌ Negative deposit should raise error
# try:
#     account.deposit(-100, 2222)
# except ValueError as e:
#     assert str(e) == "Deposit amount must be greater than 0."
#
# print("✅ All assertions passed. BankAccount working fine!")

