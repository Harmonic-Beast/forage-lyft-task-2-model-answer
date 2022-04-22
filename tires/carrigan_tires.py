from typing_extensions import Self
from tires.tire import Tire 
from abc import ABC

class CarriganTires(Tire):
    def __init__(self, worn_tire):
        self.worn_tire = worn_tire
    
    def tire_needs_to_be_serviced(self):  
        for tire in self.worn_tire:
            if tire > 0.9:
                return True
            else:
                return False
    



