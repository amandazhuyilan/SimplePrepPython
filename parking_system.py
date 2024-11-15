import unittest

class ParkSystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []
    
    def park_car(self, car : str):
        self.cars.append(car)
        self.capacity -= 1
        if self.capacity < 0:
            raise Exception("No space left!")
        return "Car parked!"
    
    def remove_car(self, car: str):
        try:
            self.cars.remove(car)
        except Exception as e:
            raise e
        return "Car out of the parking lot!"
    

class TestParkSystem(unittest.TestCase):
    def setUp(self):
        self.parking_system = ParkSystem(1)
    
    def test_park_car(self):
        response = self.parking_system.park_car("BMW X3")
        self.assertEqual(response, "Car parked!")

    def test_remove_car(self):
        self.parking_system.park_car("BMW X3")
        response = self.parking_system.remove_car("BMW X3")
        self.assertEqual(response, "Car out of the parking lot!")

    def test_error_with_full_parking_lot(self):
        self.parking_system.park_car("car 1")
        with self.assertRaises(Exception):
            self.parking_system.park_car("car 2")

    def test_error_with_none_existing_car(self):
        self.parking_system.park_car("car 3")
        with self.assertRaises(Exception):
            self.parking_system.remove_car("car 4")


if __name__ == "__main__":
    unittest.main()