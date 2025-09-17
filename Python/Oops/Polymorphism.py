# class Payment:
#
#     def pay(self,amount):
#         raise NotImplementedError
#
# class CreditCard(Payment):
#
#     def pay(self,amount):
#         print(f"paid {amount} by using creditcard")
#
# class PayPal(Payment):
#
#     def pay(self,amount):
#         print(f"paid {amount} using paypal")
#
# class GiftCard(Payment):
#
#     def pay(self,amount):
#         print(f"paid {amount} using giftcard")
#
# payments = [CreditCard(),PayPal(),GiftCard()]
# for method in payments:
#     method.pay(100)

class payment:

    def pay(self,amount):
        raise NotImplementedError

class CreditCard(payment):
    def pay(self,amount):
        print(f"paid {amount} using creditcard")

class Paypal(payment):

    def pay(self,amount):
        print(f"paid {amount} from paypal")

class Giftcard(payment):

    def pay(self,amount):
        print(f"paid {amount} from giftcard")

payments = [CreditCard(),Paypal(),Giftcard()]
for method in payments:
    method.pay(1000)