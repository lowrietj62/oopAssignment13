# -----------------------------
# Shop Class
# -----------------------------
class Shop:
    # Main system class that manages everything.

    def __init__(self, name):
        # Initialize the shop.
        self.name = name
        self.inventory = Inventory()
        self.customers = []
        self.rentals = []

    def add_customer(self, customer):
        # Adds a new customer to the shop.
        self.customers.append(customer)

    def create_rental(self, customer, equipment_type, quantity, rental_period, duration):
        # Creates a rental after checking inventory.

        if not self.inventory.is_available(equipment_type, quantity):
            print("Not enough equipment available.")
            return None

        self.inventory.rent_out(equipment_type, quantity)

        rental = Rental(customer, equipment_type, quantity, rental_period, duration)
        self.rentals.append(rental)
        return rental

    def return_rental(self, rental, coupon_code=None):
        # Processes a return and generates the final bill.

        self.inventory.return_item(rental.equipment_type, rental.quantity)

        total = rental.calculate_cost()
        total = rental.apply_discounts(total, coupon_code)

        return total

    def list_available_equipment(self):
        # Returns all currently available equipment.
        return self.inventory.display_inventory()

    def generate_report(self):
        # Generates a simple summary of shop activity.

        report = f"Shop: {self.name}\n"
        report += f"Total Customers: {len(self.customers)}\n"
        report += f"Total Rentals: {len(self.rentals)}\n"
        report += f"Available Equipment: {self.inventory.display_inventory()}\n"
        return report


# -----------------------------
# Inventory Class
# -----------------------------
class Inventory:
    # Manages all equipment stock in the shop.

    def __init__(self):
        # Initialize stock levels.
        self.stock = {
            "skis": 0,
            "snowboard": 0
        }

    def add_stock(self, equipment_type, quantity):
        # Adds equipment to inventory.
        self.stock[equipment_type] += quantity

    def is_available(self, equipment_type, quantity):
        # Checks if requested quantity is available.
        return self.stock.get(equipment_type, 0) >= quantity

    def rent_out(self, equipment_type, quantity):
        # Reduces stock when equipment is rented.
        if self.is_available(equipment_type, quantity):
            self.stock[equipment_type] -= quantity
            return True
        return False

    def return_item(self, equipment_type, quantity):
        # Increases stock when equipment is returned.
        self.stock[equipment_type] += quantity

    def display_inventory(self):
        # Displays current inventory levels.
        return self.stock


# -----------------------------
# Equipment Class
# -----------------------------
class Equipment:
    # Represents a piece of equipment.

    def __init__(self, equipment_type, brand, rental_period=0):
        # Initialize equipment details.
        self.equipment_type = equipment_type
        self.brand = brand
        self.rental_period = rental_period

    def display_info(self):
        # Displays equipment details.
        print(f"Equipment: {self.equipment_type}")
        print(f"Brand: {self.brand}")
        print(f"Rental period: {self.rental_period}")

    def calculate_cost(self):
        # Basic cost calculation (not used for final billing).
        price_per_day = 50
        return self.rental_period * price_per_day

    def is_long_term(self):
        # Checks if rental period is long-term.
        return self.rental_period > 5


# -----------------------------
# Rental Class
# -----------------------------
class Rental:
    # Represents a rental transaction.

    def __init__(self, customer, equipment_type, quantity, rental_period, duration):
        # Initialize rental details.
        self.customer = customer
        self.equipment_type = equipment_type
        self.quantity = quantity
        self.rental_period = rental_period
        self.duration = duration

    def display_info(self):
        # Displays rental details.
        print("Customer:", self.customer.name)
        print("Equipment Type:", self.equipment_type)
        print("Quantity:", self.quantity)
        print("Rental Period:", self.rental_period)
        print("Duration:", self.duration)

    def calculate_cost(self):
        # Calculates rental cost based on pricing rules.

        if self.equipment_type == "skis":
            if self.rental_period == "hourly":
                price = 15
            elif self.rental_period == "daily":
                price = 50
            else:
                price = 200
        else:  # snowboard
            if self.rental_period == "hourly":
                price = 10
            elif self.rental_period == "daily":
                price = 40
            else:
                price = 160

        return price * self.quantity * self.duration

    def apply_discounts(self, total, coupon_code=None):
        # Applies discounts based on business rules.

        # Family discount (3-5 rentals)
        if 3 <= self.quantity <= 5:
            total *= 0.75

        # Coupon discount
        if coupon_code and coupon_code.endswith("BBP"):
            total *= 0.90

        return total

    def is_long_term(self):
        # Checks if rental duration is long-term.
        return self.duration > 5


# -----------------------------
# Customer Class
# -----------------------------
class Customer:
    # Represents a customer.

    def __init__(self, name, phone, email, age):
        # Initialize customer details.
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # Validates customer name.
        if value == "":
            print("Invalid name")
        else:
            self.__name = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        # Validates phone number.
        if value == "":
            print("Invalid phone")
        else:
            self.__phone = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        # Validates email.
        if value == "":
            print("Invalid email")
        else:
            self.__email = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        # Validates age.
        if value < 0:
            print("Invalid age")
        else:
            self.__age = value

    def display_info(self):
        # Displays customer details.
        print("Customer Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Age:", self.age)

    def is_adult(self):
        # Checks if customer is an adult.
        return self.age >= 18