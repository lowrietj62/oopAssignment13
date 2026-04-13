from abc import ABC
 
class Equipment(ABC):
    
    def __init__(self, hourly_rate: float, daily_rate: float, weekly_rate: float):
        self._hourly_rate = hourly_rate
        self._daily_rate = daily_rate
        self._weekly_rate = weekly_rate
 
    def get_hourly_rate(self):
        return self._hourly_rate
 
    def get_daily_rate(self):
        return self._daily_rate
 
    def get_weekly_rate(self):
        return self._weekly_rate
 
    def get_rates(self):
        return {
            "hourly": self._hourly_rate,
            "daily": self._daily_rate,
            "weekly": self._weekly_rate,
        }
 
    def equipment_type(self):
        pass