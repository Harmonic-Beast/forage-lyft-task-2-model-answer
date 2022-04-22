import unittest
from engine.engine import Engine
from serviceable import Serviceable
from datetime import datetime
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class testNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        nubbinBattery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbinBattery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        nubbinBattery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbinBattery.needs_service())

class testSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        spindlerBattery = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(spindlerBattery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        spindlerBattery = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(spindlerBattery.needs_service())

class testCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capuletEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capuletEngine.needs_service())

class testSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        sternmanEngine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternmanEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        sternmanEngine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternmanEngine.needs_service())

class testWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughbyEngine.needs_service())


    def test_engine_should_not_be_serviced(self):
        current_mileage = 6000
        last_service_mileage = 0
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughbyEngine.needs_service())

class testCarriganTires(unittest.TestCase):
    def test_tire_should_be_services(self):
        worn_tire = 1
        carriganTire = CarriganTires(worn_tire)
        self.assertTrue(carriganTire.needs_service())

    def test_tire_should_not_be_services(self):
        worn_tire = 0.8
        carriganTire = CarriganTires(worn_tire)
        self.assertFalse(carriganTire.needs_service())

class testOctoprimeTires(unittest.TestCase):
    def test_tire_should_be_services(self):
        worn_tire = 4
        octoprimeTire = OctoprimeTires(worn_tire)
        self.assertTrue(octoprimeTire.needs_service())

    def test_tire_should_be_services(self):
        worn_tire = 2
        octoprimeTire = OctoprimeTires(worn_tire)
        self.assertFalse(octoprimeTire.needs_service())

if __name__ == '__main__':
    unittest.main()
