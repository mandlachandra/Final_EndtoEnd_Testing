class RestaurantBill:
    def __init__(self, people):
        self.people = people
        self.total = 0
        self.items = []

    def add_item(self, name, cost):
        self.items.append((name, cost))
        self.total += cost

    def show_bill(self):
        print(f"\n🍽️ Restaurant Bill for {self.people} people:\n")
        for item, cost in self.items:
            print(f"{item:<30} : ₹{cost}")
        print("-" * 40)
        print(f"Total Bill{' ' * 18} : ₹{self.total}")


# Create bill for 4 people
bill = RestaurantBill(4)

# Add orders
bill.add_item("Veg & Non-Veg Starters", 1000)
bill.add_item("Veg & Non-Veg Main Course", 2000)
bill.add_item("4 Cool Drinks", 100)
bill.add_item("4 Ice Creams", 1000)

# Print final bill
bill.show_bill()
