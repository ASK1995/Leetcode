class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.type = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if(self.type[carType] != 0):
            self.type[carType] -= 1
        else:
            return False
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)