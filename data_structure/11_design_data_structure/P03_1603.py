from typing import *


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.count = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, car: int) -> bool:
        if self.count[car] > 0:
            self.count[car] -= 1
            return True
        return False
