class Engine:
    def __init__(self, horsepower) -> None:
        self.horsepower = horsepower

    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"

class Vehicle:
    total_vehicles = 0
    def __init__(self, brand, model, engine: Engine) -> None:
        self.brand = brand
        self.model = model
        self.engine = engine

    engineObj = Engine(150)
    print(engineObj.get_engine_info())
    

    def get_details(self):
        return self.brand, self.model, self.engine.get_engine_info()
    
    @staticmethod 
    def get_vehicle_type():
        return "Generic Vehicle"

    @classmethod 
    def get_total_vehicles():
        return ""

class Car(Vehicle):
    def __init__(self, brand: str, model: str, engine: Engine, seats: int):
        super().__init__(brand, model, engine)
        self.seats = seats
        
    def get_details(self):
        return f"{super().get_details()} - Seats: {self.seats}"