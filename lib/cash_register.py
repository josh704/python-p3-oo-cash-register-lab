#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []  
        self.last_transaction = 0
        self.discount = discount 

    def add_item(self, title, price, quantity=1):
        try:
            price = float(price)  
            quantity = int(quantity)  
        except ValueError:
            raise ValueError("Price and quantity must be numeric values.")

        for _ in range(quantity):
            self.items.append(title)

        self.total += price * quantity
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")
        return self.total

    def void_last_transaction(self):
        self.total -= self.last_transaction
        if self.items:
            self.items.pop()
        self.last_transaction = 0.0

    def get_items(self):
        return self.items
