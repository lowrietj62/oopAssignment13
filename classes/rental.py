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
 
    # ADDED: returns a human-readable duration string (e.g. "2 hours", "1 day", "3 weeks")
    def _duration_label(self):
        unit_map = {
            "hourly": "hour",
            "daily":  "day",
            "weekly": "week",
        }
        unit = unit_map.get(self._rental_type, self._rental_type)
        label = f"{self._duration} {unit}"
        if self._duration != 1:
            label += "s"
        return label
 
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
        print(f"  Duration  : {self._duration_label()}")
        print(f"  Rate/item : ${base:.2f} (best price)")
        print(f"  Subtotal  : ${subtotal:.2f}")
        if self._family_discount_applies():
            print(f"  Family    : -25%")
        if self._coupon_discount_applies():
            print(f"  Coupon    : -10% ({self._coupon_code})")
        print(f"  TOTAL     : ${total:.2f}")
        print(f"{'='*38}\n")