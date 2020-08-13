from abc import ABCMeta, abstractmethod


class Customer(metaclass=ABCMeta):

    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None
        self.bill_id = None

    @abstractmethod
    def calculate_bill_amount(self):
        pass

    def get_customer_name(self):
        return self.__customer_name


class OccasionalCustomer(Customer):

    __counter = 1000

    def __init__(self, customer_name, distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms = distance_in_kms
        OccasionalCustomer.__counter += 1
        self.bill_id = "O" + str(OccasionalCustomer.__counter)

    def validate_distance_in_kms(self):
        if self.get_distance_in_kms() >= 1 and self.get_distance_in_kms() <= 5:
            return True
        else:
            return False

    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            delivery_charge = 0
            if self.__distance_in_kms >= 1 and self.__distance_in_kms <= 2:
                delivery_charge = 5 * self.__distance_in_kms
            elif self.__distance_in_kms > 2 and self.__distance_in_kms <= 5:
                delivery_charge = 7.5 * self.get_distance_in_kms()

            self.bill_amount = 50 + delivery_charge
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount

    def get_distance_in_kms(self):
        return self.__distance_in_kms


class RegularCustomer(Customer):

    __counter = 100

    def __init__(self, customer_name, no_of_tiffin):
        super().__init__(customer_name)
        self.__no_of_tiffin = no_of_tiffin
        RegularCustomer.__counter += 1
        self.bill_id = "R" + str(RegularCustomer.__counter)

    def validate_no_of_tiffin(self):
        if self.get_no_of_tiffin() >= 1 and self.get_no_of_tiffin() <= 7:
            return True
        else:
            return False

    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount = 7 * 50 * self.get_no_of_tiffin()
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin
