# Design a Parking Lot System
# Problem: Implement a simple class structure for a parking lot system where you can park and remove cars. 
# Include different types of vehicles and keep track of the available parking spaces.

import unittest

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []

    def park_car(self, car_to_be_parked: str) -> bool:
        """
        park the damn car

        args:
            car_to_be_parked (str): the car to be parked
        """
        if len(self.cars) > self.capacity:
            return "Parking lot full!"
        else:
            self.capacity -= 1
            self.cars.append(car_to_be_parked)
            return "Car parked!"

    def remove_car(self, car_to_be_removed: str) -> bool:
        if car_to_be_removed not in self.cars:
            return "Car to be removed not available!"

        self.cars.remove(car_to_be_removed)
        self.capacity += 1
        return "Car removed!"

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.lot = ParkingLot(100)

    def test_park_car(self):
        response = self.lot.park_car("BMW X3")
        self.assertEqual(response, "Car parked!")

    def test_remove_car(self):
        response = self.lot.remove_car("BMW X3")
        self.assertEqual(response, "Car removed!")

    def test_remove_car_fail(self):
        response = self.lot.remove_car("BMW X1")
        self.assertEqual(response, "Car to be removed not available!")

if __name__ == "__main__":
    unittest.main()