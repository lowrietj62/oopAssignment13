# All code combined into a single file

from abc import ABC
#--------------------------------------------------------------------------
# Class Name: Equipment
# Description: Abstract base class for rental equipment; stores hourly, daily, and weekly rates
#--------------------------------------------------------------------------
class Equipment(ABC):
    
    def __init__(self, hourly_rate: float, daily_rate: float, weekly_rate: float):
        self._hourly_rate = hourly_rate
        self._daily_rate = daily_rate
        self._weekly_rate = weekly_rate
 
    def get_hourly_rate(self):
        return self._hourly_rate
 
    def get_daily_rate(self):
        return self._daily_rate
 
    def get_weekly_rate(self):
        return self._weekly_rate
 
    def get_rates(self):
        return {
            "hourly": self._hourly_rate,
            "daily": self._daily_rate,
            "weekly": self._weekly_rate,
        }
 
    def equipment_type(self):
        pass


#--------------------------------------------------------------------------
# Class Name: Inventory
# Description: Tracks available skis and snowboards; handles stock checks and updates
#--------------------------------------------------------------------------
class Inventory:

    def __init__(self, skis_available=20, snowboards_available=15):
        self.skis_available = skis_available
        self.snowboards_available = snowboards_available

    # ADDED: rental_shop.py was already calling get_stock(), so this was added to match
    def get_stock(self):
        return self.skis_available, self.snowboards_available

    def check_availability(self, equipment_type, quantity):
        if equipment_type.lower() == "ski":
            return self.skis_available >= quantity
        elif equipment_type.lower() == "snowboard":
            return self.snowboards_available >= quantity
        else:
            return False

    # CHANGED: added rent=True/False parameter so this method handles both
    # renting out (deduct) and returning (add back), matching what rental_shop.py expected
    def update_stock(self, equipment_type, quantity, rent=True):
        """
        rent=True  -> deduct stock (renting out)
        rent=False -> add stock back (returning)
        """
        if equipment_type.lower() == "ski":
            if rent:
                self.skis_available -= quantity
            else:
                self.skis_available += quantity
        elif equipment_type.lower() == "snowboard":
            if rent:
                self.snowboards_available -= quantity
            else:
                self.snowboards_available += quantity

    def display_inventory(self):
        print("Current Inventory:")
        print(f"Skis available: {self.skis_available}")
        print(f"Snowboards available: {self.snowboards_available}")


from classes.equipment import Equipment
#--------------------------------------------------------------------------
# Class Name: Ski
# Description: Concrete subclass of Equipment with hard-coded ski rates
#--------------------------------------------------------------------------
class Ski(Equipment):
    
    def __init__(self):
        super().__init__(hourly_rate=15.0, daily_rate=50.0, weekly_rate=200.0)
 
    def equipment_type(self) -> str:
        return "Ski"
    

from classes.equipment import Equipment
#--------------------------------------------------------------------------
# Class Name: Snowboard
# Description: Concrete subclass of Equipment with hard-coded snowboard rates
#--------------------------------------------------------------------------
from classes.equipment import Equipment
 
class Snowboard(Equipment):
    
    def __init__(self):
        super().__init__(hourly_rate=10.0, daily_rate=40.0, weekly_rate=160.0)
 
    def equipment_type(self) -> str:
        return "Snowboard"
    

#--------------------------------------------------------------------------
# Class Name: Rental
# Description: Represents a single rental transaction; handles billing, discounts, and bill printing
#--------------------------------------------------------------------------
class Rental:
    
    # CHANGED: added duration and coupon_code params - needed for billing logic
    def __init__(self, item_type, quantity, rental_type, duration, coupon_code=""):
        self._item_type = item_type        # "Ski" or "Snowboard"
        self._quantity = quantity
        self._rental_type = rental_type    # "hourly", "daily", "weekly"
        self._duration = duration          # number of hours/days/weeks
        
        # ADDED: strip and uppercase so comparisons are consistent
        self._coupon_code = coupon_code.strip().upper()
 
        # ADDED: rates stored here so calculate_bill() can look them up
        self._rates = {
            "Ski":        {"hourly": 15.0, "daily": 50.0, "weekly": 200.0},
            "Snowboard":  {"hourly": 10.0, "daily": 40.0, "weekly": 160.0},
        }
    
    # ------------------------------------------------------------------
    # Getters (used by Rental_Shop)
    # ------------------------------------------------------------------
 
    # ADDED: rental_shop.py was already calling these, so they needed to exist
    def get_equipment_type(self):
        return self._item_type
 
    def get_quantity(self):
        return self._quantity
 
    # CHANGED: added duration and coupon to the returned dict to match new fields
    def get_detail(self):
        return {
            "item":     self._item_type,
            "qty":      self._quantity,
            "type":     self._rental_type,
            "duration": self._duration,
            "coupon":   self._coupon_code,
        }
 
    # ------------------------------------------------------------------
    # Pricing helpers
    # ------------------------------------------------------------------
 
    # ADDED: finds the cheapest per-item rate given the period type and duration
    def _best_price_per_item(self):
        """Returns the cheapest per-item cost based on duration and period."""
        rates = self._rates[self._item_type]
 
        if self._rental_type == "hourly":
            hourly_total = rates["hourly"] * self._duration
            # Daily rate might be cheaper at 4+ hours
            return min(hourly_total, rates["daily"])
 
        elif self._rental_type == "daily":
            daily_total = rates["daily"] * self._duration
            # Check if splitting into full weeks saves money
            full_weeks = self._duration // 7
            remaining_days = self._duration % 7
            if full_weeks > 0:
                weekly_option = (rates["weekly"] * full_weeks) + (rates["daily"] * remaining_days)
                return min(daily_total, weekly_option)
            return daily_total
 
        else:  # weekly
            return rates["weekly"] * self._duration
 
    # ADDED: family discount applies for 3-5 total items rented
    def _family_discount_applies(self):
        return 3 <= self._quantity <= 5
 
    # ADDED: coupon discount applies if code ends in "BBP"
    def _coupon_discount_applies(self):
        return self._coupon_code.endswith("BBP")
 
    # ------------------------------------------------------------------
    # Calculate Bill
    # ------------------------------------------------------------------
 
    # CHANGED: was a pass/stub - filled in with best price, family, and coupon logic
    def calculate_bill(self):
        subtotal = self._best_price_per_item() * self._quantity
 
        discount = 0.0
        if self._family_discount_applies():
            discount += 0.25
        if self._coupon_discount_applies():
            discount += 0.10
 
        total = subtotal * (1 - discount)
        return round(total, 2)
 
    # ADDED: prints a formatted bill breakdown when equipment is returned
    def print_bill(self):
        base = self._best_price_per_item()
        subtotal = base * self._quantity
        total = self.calculate_bill()
 
        print(f"\n{'='*38}")
        print(f"  RENTAL BILL")
        print(f"{'='*38}")
        print(f"  Equipment : {self._item_type}")
        print(f"  Quantity  : {self._quantity}")
        print(f"  Period    : {self._rental_type} x {self._duration}")
        print(f"  Rate/item : ${base:.2f} (best price)")
        print(f"  Subtotal  : ${subtotal:.2f}")
        if self._family_discount_applies():
            print(f"  Family    : -25%")
        if self._coupon_discount_applies():
            print(f"  Coupon    : -10% ({self._coupon_code})")
        print(f"  TOTAL     : ${total:.2f}")
        print(f"{'='*38}\n")


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
    

#--------------------------------------------------------------------------
# Main
#--------------------------------------------------------------------------
from classes.equipment import Equipment
from classes.inventory import Inventory
from classes.rental import Rental
from classes.rental_shop import Rental_Shop
from classes.skis import Ski
from classes.snowboards import Snowboard

# ------------------------------------------------------------------
# Setup shop
# ------------------------------------------------------------------
shop = Rental_Shop(skis=10, snowboards=8)

print("=== SKI RENTAL SHOP ===")
shop.display_inventory()

# ------------------------------------------------------------------
# Test rentals
# ------------------------------------------------------------------

# Basic hourly ski rental
r1 = Rental("Ski", quantity=2, rental_type="hourly", duration=2)
shop.process_rental(r1)

# Best price: 4 hours vs daily rate
r2 = Rental("Ski", quantity=1, rental_type="hourly", duration=4)
shop.process_rental(r2)

# Family discount (3 snowboards)
r3 = Rental("Snowboard", quantity=3, rental_type="daily", duration=1)
shop.process_rental(r3)

# Coupon code ending in BBP
r4 = Rental("Ski", quantity=1, rental_type="weekly", duration=1, coupon_code="SKIBBP")
shop.process_rental(r4)

# Family + coupon stacked
r5 = Rental("Snowboard", quantity=4, rental_type="daily", duration=2, coupon_code="MYBBP")
shop.process_rental(r5)

# Insufficient stock
r6 = Rental("Ski", quantity=100, rental_type="daily", duration=1)
shop.process_rental(r6)

print("\n--- Inventory after rentals ---")
shop.display_inventory()

# ------------------------------------------------------------------
# Return equipment and print bills
# ------------------------------------------------------------------
print("\n--- Returning all rentals ---")
for r in [r1, r2, r3, r4, r5]:
    shop.return_rental(r)

print("\n--- Final Inventory ---")
shop.display_inventory()


