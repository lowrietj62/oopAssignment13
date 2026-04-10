from inventory import Inventory

#--------------------------------------------------------------------------
# Class Name: Rental_Shop
# Description: The main class for handling anything to do with the ski rental shop
#--------------------------------------------------------------------------

class Rental_Shop:
    
    def __init__(self, skis = 0, snowboards = 0):
        
        # Encapsulation: Inventory object is stored internally
        self._inventory = Inventory(skis, snowboards)

        # List to track active rentals
        self._activeRentals = []

    # Display Inventory
    def display_inventory(self): 

        skis, snowboards = self._inventory.get_stock()

        print("Current Inventory:")
        print("Skis Available", skis)
        print("Snowboards Available", snowboards)


