class Vehicle:

    def __init__(self, mileage=0, fuel_left=5):
        self.mileage = mileage
        self.fuel_left = fuel_left
        self.initial_fuel = 6

    def set_mileage(self, mileage):
        self.mileage = mileage

    def fuel_left(self, fuel_left):
        self.fuel_left = fuel_left

    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left > 5:
            return (self.fuel_left - 5) * self.mileage
        else:
            return 0

    def identify_distance_travelled(self, initial_fuel):
        return (initial_fuel - self.fuel_left) * self.mileage


v1 = Vehicle(20, 12)
print(v1.identify_distance_that_can_be_travelled())
