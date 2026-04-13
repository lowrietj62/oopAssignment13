class Rental:
    
    def __init__(self,item_type,quantity,rental_type):
        self._item_type = item_type
        self._quantity = quantity
        self._rental_type = rental_type  # hourly, daily, weekly
        
    def get_detail(self):
        return{ 
            "item" : self._item_type,
            "qty" : self._quantity,
            "type" : self._rental_type,
        }
    
    def calculate_bill():
        