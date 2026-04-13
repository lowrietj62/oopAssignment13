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