from typing_extensions import Self
from tires.tire import Tire 
from abc import ABC

class OctoprimeTires(Tire):
    def __init__(self, worn_tire):
        self.worn_tire = worn_tire
    
    def tire_needs_to_be_serviced(self):  
        if sum(self.worn_tire) > 3:
            return True
        else:
            return False
    



