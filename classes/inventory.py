
class Inventory:
    def __init__(self, skis_available=20, snowboards_available=15):
        self.skis_available = skis_available
        self.snowboards_available = snowboards_available

    def check_availability(self, equipment_type, quantity):
        if equipment_type.lower() == "ski":
            return self.skis_available >= quantity
        elif equipment_type.lower() == "snowboard":
            return self.snowboards_available >= quantity
        else:
            return False

    def update_stock(self, equipment_type, quantity):
        if equipment_type.lower() == "ski":
            self.skis_available += quantity
        elif equipment_type.lower() == "snowboard":
            self.snowboards_available += quantity

    def rent_items(self, equipment_type, quantity):
        if self.check_availability(equipment_type, quantity):
            if equipment_type.lower() == "ski":
                self.skis_available -= quantity
            elif equipment_type.lower() == "snowboard":
                self.snowboards_available -= quantity
            return True
        return False

    def display_inventory(self):
        print("Current Inventory:")
        print(f"Skis available: {self.skis_available}")
        print(f"Snowboards available: {self.snowboards_available}")