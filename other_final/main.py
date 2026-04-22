"""
main.py - Ski & Snowboard Rental Shop CLI
Orchestrates the rental shop application using classes from classes.py.
All heavy logic lives in the classes; main handles I/O and flow.
"""
 
from other_final.FinalProjectPt1_HW import Shop, Customer, Rental
import other_final.FinalProjectPt1_HW as Classes

# Menu Actions
def action_new_rental(shop: Shop, day_stats: dict):
    
    """
    Menu option 1 — New Customer Rental.
    """
    
    print("\n" + "=" * 45)
    print("  NEW CUSTOMER RENTAL")
    print("=" * 45)
 
    # Gather rental details
    equipment_type = Classes.get_equipment_choice()
    quantity       = Classes.get_positive_int("  Enter quantity: ")
    rental_period  = Classes.get_rental_period()
    duration       = Classes.get_positive_int(f"  Enter number of {rental_period}s: ")
    coupon_raw     = input("  Coupon code (press Enter to skip): ").strip()
    coupon_code    = coupon_raw if coupon_raw else None
 
    # Check inventory
    if not shop.inventory.is_available(equipment_type, quantity):
        print(f"\n  > Sorry — not enough {equipment_type} available.")
        print(f"    Current stock: {shop.inventory.stock.get(equipment_type, 0)}")
        return
 
    # Generate estimate via a temporary Rental object
    # (No Customer object needed yet — we show the price first)
    temp_customer = Customer("Preview", "0000000000", "preview@example.com", 18)
    temp_rental   = Rental(temp_customer, equipment_type, quantity, rental_period, duration)
 
    total_before  = temp_rental.calculate_cost()
    final_total   = temp_rental.apply_discounts(total_before, coupon_code)
    discount_amt  = total_before - final_total
 
    print("\n  ── Rental Estimate ──────────────────────")
    print(f"    Equipment   : {equipment_type.capitalize()}")
    print(f"    Quantity    : {quantity}")
    print(f"    Period      : {rental_period.capitalize()}")
    print(f"    Duration    : {duration} {rental_period}(s)")
    print(f"    Subtotal    : ${total_before:.2f}")
    if discount_amt > 0:
        print(f"    Discount    : -${discount_amt:.2f}")
    print(f"    TOTAL       : ${final_total:.2f}")
    print("  ─────────────────────────────────────────")
 
    proceed = input("\n  Proceed with rental? (y/n): ").strip().lower()
    if proceed != "y":
        print("  Rental cancelled.")
        return
 
    # Collect customer info
    print("\n  Enter customer information:")
    last_name = Classes.get_nonempty_string("    Last name    : ")
    phone     = Classes.get_phone(          "    Phone number : ")
    email     = Classes.get_email(          "    Email        : ")
    age       = Classes.get_age(            "    Age          : ")
 
    customer = Customer(last_name, phone, email, age)
    shop.add_customer(customer)
 
    # Create the real rental (reduces inventory)
    rental = shop.create_rental(customer, equipment_type, quantity, rental_period, duration)
    if rental is None:
        print("  > Rental could not be completed (inventory issue).")
        return
 
    # Attach coupon so it can be applied on return
    rental.coupon_code = coupon_code
 
    # ── Update day stats ──
    if equipment_type == "skis":
        day_stats["total_skis_rented"] += quantity
    else:
        day_stats["total_snowboards_rented"] += quantity
 
    print(f"\n  Rental created! Rental ID: #{id(rental) % 100000}")
    print(f"    Customer: {customer.name}  |  Phone: {customer.phone}")
