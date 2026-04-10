from inventory import Inventory

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
        self._activeRentals = []

    # Display Inventory
    def display_inventory(self): 

        skis, snowboards = self._inventory.get_stock()

        print("Current Inventory:")
        print("Skis Available", skis)
        print("Snowboards Available", snowboards)

    # Process Rental
    def process_rental(self, rental):
        
        equipment_type = rental.getEquipmentType()
        quantity = rental.getQuantity()

        # Check availability
        available  = self._inventory.check_availability(equipment_type, quantity)

        if available == True:
            
            # Update inventory
            self._inventory.update_stock(equipment_type, quantity, rent = True)

            # Add rental to active list
            self._activeRentals.appent(rental)

            print("Rental processed succesfully")
            return rental      
         
        else:
            print("Requested quantity not available.")
            return None
    
    # Return Rental (Triggers Billing)
    def return_rental(self, rental):

        found = False

        # Check if rental exists
        for r in self._activeRentals:
            if r == rental:
                found = True

        if found == True:

            equipment_type = rental.getEquipmentType()
            quantity = rental.getQuantity()

            # Update inventory (return items)
            self._inventory.update_stock(equipment_type, quantity, rent = False)

            # Calculate bill
            bill = rental.calculate_bill()

            # Remove rental
            for r in self._activeRentals:
                if r == rental:
                    self._activeRentals.remove(r)
                    break

            print("Rental returned successfully.")
            print("Total Bill: $", bill)

            return bill
        
        else:
            print("Rental not found.")
            return None
        
    # Getter for active rentals
    def getActiveRentals(self):
        return self._activeRentals
    
    # Getter for inventory
    def getInventory(self):
        return self._inventory