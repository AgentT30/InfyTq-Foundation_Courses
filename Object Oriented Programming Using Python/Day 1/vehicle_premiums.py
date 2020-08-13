class Vehicle:

    def __init__(self):
        self.__vehicle_type = ""
        self.__v_id = 0
        self.__vehicle_cost = 0
        self.__premium_amount = 0

    def set_vehicle_id(self, v_id):
        self.__v_id = v_id

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def set_premium_amount(self):
        self.__premium_amount = 0

    def get_vehicle_id(self):
        return self.__v_id

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def calculate_premium(self):
        if self.__vehicle_type.lower() == "two wheeler":
            return (self.__vehicle_cost * 0.02)
        elif self.__vehicle_type.lower() == "four wheeler":
            return (self.__vehicle_cost * 0.06)
        else:
            return 'Invalid Vehicle Type'


v1 = Vehicle()
v1.set_vehicle_type('two wheeler')
v1.set_vehicle_id(1000)
v1.set_vehicle_cost(50000)
print(v1.calculate_premium())
