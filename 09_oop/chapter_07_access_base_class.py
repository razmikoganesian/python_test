# Accesing Base class

class BaseCalss:
    def __init__(self, type, strength) -> None:
        self.type = type
        self.strength = strength

class ChildClass(BaseCalss):
    def __init__(self, type, strength, sugar_level) -> None:
        # super().__init__(type, strength)
        self.type = type
        self.strength = strength
        self.sugar_level = sugar_level
# Examples Code duplication aviding

 # Explicit call
class ChildClass1(BaseCalss):
    def __init__(self, type, strength, sugar_level) -> None:
        # super().__init__(type, strength)
        BaseCalss.__init__(self, type, strength) # Explicit call

        self.sugar_level = sugar_level
# super

class ChildClass2(BaseCalss):
    def __init__(self, type, strength, sugar_level) -> None:
        super().__init__(type, strength)
        self.sugar_level = sugar_level