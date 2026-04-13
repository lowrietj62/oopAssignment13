from classes.equipment import Equipment
 
class Ski(Equipment):
    
    def __init__(self):
        super().__init__(hourly_rate=15.0, daily_rate=50.0, weekly_rate=200.0)
 
    def equipment_type(self) -> str:
        return "Ski"