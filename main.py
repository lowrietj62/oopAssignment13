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