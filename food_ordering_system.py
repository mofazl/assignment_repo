#STUDENT1: MOHAMMED FAZLUR RAHMAN
#STUDENTID: 426001122
#STUDENT2:
#STUDENTID:
#STUDENT3:
#STUDENTID:
"""
TASK 1: A dictionary called 'menu' containing three categories: 'Drinks', 'Entrees', and 'Side Item'.
Each category contains at least three items with their corresponding prices as float values.
"""
menu = {
    "Drinks": {
        "Coffee": 2.50, 
        "Tea": 2.00, 
        "Juice": 3.00
    }, 
    "Entrees": {
        "Sandwich": 5.00, 
        "Salad": 4.50, 
        "Soup": 3.50
    }, 
    "Side Item": {
        "Fries": 2.00, 
        "Fruit": 2.50, 
        "Chips": 1.50
        }
}

class Combo:
    __slots__ = ['drink', 'entree', 'side_item','total_price']
    def __init__(self, drink, entree, side_item, total_price):
        self.drink = drink
        self.entree = entree
        self.side_item = side_item
        self.total_price = 0.0

    def get_total(self):
        if self.drink:
            self.total_price+=menu['Drinks'][self.drink]
        if self.entree:
            self.total_price+=menu['Entrees'][self.entree]
        if self.side_item:
            self.total_price+=menu['Side Item'][self.side_item]
        return self.total_price
    
    def display_combo(self):
        print("Combo Details:")
        print(f"Drink: {self.drink if self.drink else 'None'} | "
              f"Entrée: {self.entree if self.entree else 'None'} | "
              f"Side: {self.side_item if self.side_item else 'None'}")
        print(f"Total Combo Price: {self.get_total()} AED")

# Example usage:
combo1 = Combo("Coffee", "Sandwich", "Fries",0)
combo1.display_combo()