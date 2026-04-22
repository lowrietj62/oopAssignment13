"""
main.py - Ski & Snowboard Rental Shop CLI
Orchestrates the rental shop application using classes from classes.py.
All heavy logic lives in the classes; main handles I/O and flow.
"""
 
from FinalProjectPt1_HW import Shop, Customer, Rental
import FinalProjectPt1_HW as Classes

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
    
    # Check inventory
    if not shop.inventory.is_available(equipment_type, quantity):
        print(f"\n  > Sorry — not enough {equipment_type} available.")
        print(f"    Current stock: {shop.inventory.stock.get(equipment_type, 0)}")
        return
    
    rental_period  = Classes.get_rental_period()
    period_label = {"hourly": "hours", "daily": "days", "weekly": "weeks"}
    duration = Classes.get_positive_int(f"  Enter number of {period_label[rental_period]}: ")
    coupon_raw     = input("  Coupon code (press Enter to skip): ").strip()
    coupon_code    = coupon_raw if coupon_raw else None
 
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
    print(f"    Duration    : {duration} {period_label[rental_period]}")
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

def action_rental_return(shop: Shop, day_stats: dict):
    
    """
    Menu option 2 — Rental Return
    """
    
    print("\n" + "=" * 45)
    print("  RENTAL RETURN")
    print("=" * 45)
 
    if not shop.rentals:
        print("  No active rentals on record.")
        return
 
    phone = Classes.get_phone("  Enter customer phone number: ")
 
    # Find all rentals matching this phone number
    matching = [r for r in shop.rentals if r.customer.phone == phone]
 
    if not matching:
        print("  > No rental found for that phone number.")
        return
 
    # If multiple rentals found, let staff pick
    if len(matching) > 1:
        print(f"\n  Found {len(matching)} rental(s) for {phone}:")
        for i, r in enumerate(matching, 1):
            print(f"    [{i}] {r.customer.name}  |  {r.equipment_type.capitalize()} x{r.quantity}"
                  f"  |  {r.rental_period.capitalize()} x{r.duration}")
        while True:
            try:
                sel = int(input("  Select rental to return (number): ").strip())
                if 1 <= sel <= len(matching):
                    rental = matching[sel - 1]
                    break
                print("  > Invalid selection.")
            except ValueError:
                print("  > Please enter a number.")
    else:
        rental = matching[0]
 
    # Calculate costs
    period_label = {"hourly": "hours", "daily": "days", "weekly": "weeks"}
    total_before  = rental.calculate_cost()
    coupon_code   = getattr(rental, "coupon_code", None)
    final_total   = rental.apply_discounts(total_before, coupon_code)
    discount_amt  = total_before - final_total
 
    # Display invoice
    print("\n  ── INVOICE ──────────────────────────────")
    print(f"    Customer    : {rental.customer.name}")
    print(f"    Phone       : {rental.customer.phone}")
    print(f"    Equipment   : {rental.equipment_type.capitalize()} x{rental.quantity}")
    print(f"    Rental Time : {rental.duration} {period_label[rental.rental_period]}")
    print(f"    Subtotal    : ${total_before:.2f}")
    if discount_amt > 0:
        print(f"    Discount    : -${discount_amt:.2f}")
        if coupon_code:
            print(f"    Coupon      : {coupon_code}")
    print(f"    TOTAL DUE   : ${final_total:.2f}")
    print("  ─────────────────────────────────────────")
 
    confirm = input("\n  Confirm return? (y/n): ").strip().lower()
    if confirm != "y":
        print("  Return cancelled.")
        return
 
    # Process return (restores inventory, removes from active list)
    shop.return_rental(rental, coupon_code)
    shop.rentals.remove(rental)
 
    day_stats["total_revenue"] += final_total
 
    print(f"\n  > Return processed. Revenue collected: ${final_total:.2f}")

def action_show_inventory(shop: Shop):
    
    """
    Menu option 3 — Show Inventory
    """
    
    print("\n" + "=" * 45)
    print("  CURRENT INVENTORY")
    print("=" * 45)
    inv = shop.list_available_equipment()
    print(f"    Skis       : {inv.get('skis', 0)}")
    print(f"    Snowboards : {inv.get('snowboard', 0)}")
    print("=" * 45)
 
 
def action_end_of_day(shop: Shop, day_stats: dict):
    
    """
    Menu option 4 — End of Day report
    """
    
    print("\n" + "=" * 45)
    print("  END OF DAY REPORT")
    print("=" * 45)
    print(f"    Shop              : {shop.name}")
    print(f"    Total Skis Rented : {day_stats['total_skis_rented']}")
    print(f"    Total SBs Rented  : {day_stats['total_snowboards_rented']}")
    print(f"    Total Revenue     : ${day_stats['total_revenue']:.2f}")
    print("=" * 45)
    print("\n  Thanks for using the rental system. Goodbye!\n")


# Setup
 
def setup_shop():
    
    """
    Gather shop name and starting inventory on launch
    """
    
    print("=" * 45)
    print("  SKI & SNOWBOARD RENTAL SYSTEM")
    print("=" * 45)
    shop_name = Classes.get_nonempty_string("  Shop name: ")
    shop      = Shop(shop_name)
 
    print("\n  Set starting inventory:")
    ski_stock        = Classes.get_positive_int("    Number of Skis       : ")
    snowboard_stock  = Classes.get_positive_int("    Number of Snowboards : ")
 
    shop.inventory.add_stock("skis",       ski_stock)
    shop.inventory.add_stock("snowboard",  snowboard_stock)
 
    print(f"\n  > '{shop_name}' is open for business!")
    return shop
 
# Main loop
 
def main():
    
    shop = setup_shop()
 
    # Day-level counters (tracked in main — not business logic)
    day_stats = {
        "total_skis_rented":       0,
        "total_snowboards_rented": 0,
        "total_revenue":           0.0,
    }
 
    while True:
        print("\n" + "─" * 45)
        print(f"  {shop.name.upper()} — MAIN MENU")
        print("─" * 45)
        print("  [1] New Customer Rental")
        print("  [2] Rental Return")
        print("  [3] Show Inventory")
        print("  [4] End of Day")
        print("─" * 45)
 
        choice = input("  Select an option: ").strip()
 
        if choice == "1":
            action_new_rental(shop, day_stats)
        elif choice == "2":
            action_rental_return(shop, day_stats)
        elif choice == "3":
            action_show_inventory(shop)
        elif choice == "4":
            action_end_of_day(shop, day_stats)
            break
        else:
            print("  > Invalid choice. Please select 1–4.")
 
 
if __name__ == "__main__":
    main()
