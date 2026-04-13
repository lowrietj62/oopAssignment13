from classes.inventory import Inventory

#--------------------------------------------------------------------------
# Class Name: Rental_Shop
# Description: The main class for handling anything to do with the ski rental shop
#--------------------------------------------------------------------------

class Rental_Shop:
    
    #Initialization
    def __init__(self, skis = 0, snowboards = 0):
        
        # Encapsulation: Inventory object is stored internally
        self._inventory = Inventory(skis, snowboards)

        # List to track active rentals
        self._active_rentals = []

    # Display Inventory
    # FIXED: Made an adjustment to fit with the changes done in inventory class
    def display_inventory(self):
        self._inventory.display_inventory()

    # Process Rental
    def process_rental(self, rental):
        
        equipment_type = rental.get_equipment_type()
        quantity = rental.get_quantity()

        # Check availability
        available  = self._inventory.check_availability(equipment_type, quantity)

        if available:
            
            # CHANGED: update_stock now takes rent=True to deduct stock on rental
            self._inventory.update_stock(equipment_type, quantity, rent=True)
 
            # CHANGED: fixed typo from original - appent -> append
            self._active_rentals.append(rental)
 
            print("Rental processed successfully.")
            return rental
         
        else:
            print("Requested quantity not available.")
            return None
    
    # Return Rental (Triggers Billing)
    def return_rental(self, rental):

        # CHANGED: simplified from original for loop + found flag to a direct membership check
        if rental not in self._active_rentals:
            print("Rental not found.")
            return None

        equipment_type = rental.get_equipment_type()
        quantity = rental.get_quantity()
 
        # CHANGED: update_stock now takes rent=False to add stock back on return
        self._inventory.update_stock(equipment_type, quantity, rent=False)
 
        # ADDED: print_bill() called here so the bill displays on return
        rental.print_bill()
        bill = rental.calculate_bill()
 
        # Remove rental from active list
        self._active_rentals.remove(rental)
 
        print("Rental returned successfully.")
        return bill
    
    # Getter for active rentals
    def get_active_rentals(self):
        return self._active_rentals
    
    # Getter for inventory
    def get_inventory(self):
        return self._inventory