class Mechanic:

    def __init__(self, mechanic_id, specialization, vehicle_count):
        self.__mechanic_id = mechanic_id
        self.__specialization = specialization
        self.__vehicle_count = vehicle_count

    def set_mechanic_id(self, mechanic_id):
        self.__mechanic_id = mechanic_id

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def set_vehicle_count(self, vehicle_count):
        self.__vehicle_count = vehicle_count

    def get_mechanic_id(self):
        return self.__mechanic_id

    def get_specialization(self):
        return self.__specialization

    def get_vehicle_count(self):
        return self.__vehicle_count


class VehicleService():

    def __init__(self, mechanic_list):
        self.__mechanic_list = mechanic_list

    def assign_vehicle_for_service(self, mechanic_id, vehicle_type):
        if mechanic_id in self.__mechanic_list:
            if vehicle_type in self.__mechanic_list:
                Mechanic.set_vehicle_count += 1
            else:
                raise InvalidMechanicSpecializationException
        else:
            raise InvalidMechanicIdException


m1 = Mechanic(101, 'TW', 1)
m2 = Mechanic(102, 'FW', 0)
m3 = Mechanic(103, 'TW', 4)
m4 = Mechanic(104, 'FW', 2)
m5 = Mechanic(105, 'FW', 1)

try:
    VehicleService([m1, m2, m3, m4, m5])
except InvalidMechanicIdException:
    print("Invalid Mechanic ID")
except InvalidMechanicSpecializationException:
    print("Invalid Mechanic Specialization")
