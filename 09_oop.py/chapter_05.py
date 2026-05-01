from operator import truediv


class SmartDevice:
    brand = "HomeTech"
    
    def __init__ (self, device_name: str, power_status: bool ):
        self.brand = "CustomBrand"
        self.device_name = device_name
        self.power_status = power_status


    def get_status(self):
        status = "ON" if self.power_status else "OFF"
        return f"{self.device_name} is {status} - {self.brand}"
    


a = SmartDevice("Fan", False)
b = SmartDevice("AC", True)
print(a.get_status())
print(b.get_status())