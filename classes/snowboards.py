from classes.equipment import Equipment
 
class Snowboard(Equipment):
    
    def __init__(self):
        super().__init__(hourly_rate=10.0, daily_rate=40.0, weekly_rate=160.0)
 
    def equipment_type(self) -> str:
        return "Snowboard"