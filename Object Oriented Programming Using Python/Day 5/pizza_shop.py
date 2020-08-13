class Customer:

    def __init__(self, customer_name, quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity

    def validate_quantity(self):
        if self.__quantity >= 1 and self.__quantity <= 5:
            return True
        else:
            return False

    def get_customer_name(self):
        return self.__customer_name

    def get_quantity(self):
        return self.__quantity


class Pizzaservice:

    counter = 100

    def __init__(self, customer, pizza_type, additional_topping=False):
        self.__service_id = None
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = None

    def validate_pizza_type(self):
        if self.__pizza_type.lower() == "small" or self.__pizza_type.lower() == "medium":
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            Pizzaservice.counter += 1
            if self.__pizza_type.lower() == "small":
                self.pizza_cost = 150 * self.__customer.get_quantity()
                if self.__additional_topping:
                    self.pizza_cost += 35 * self.__customer.get_quantity()
                self.__service_id = "S" + str(Pizzaservice.counter)
            elif self.__pizza_type.lower() == "medium":
                self.pizza_cost = 200 * self.__customer.get_quantity()
                if self.__additional_topping:
                    self.pizza_cost += 50 * self.__customer.get_quantity()
                    self.__service_id = "M" + str(Pizzaservice.counter)
        else:
            self.pizza_cost = -1

    def get_service_id(self):
        return self.__service_id

    def get_pizza_type(self):
        return self.__pizza_type

    def get_customer(self):
        return self.__customer

    def get_additional_topping(self):
        return self.__additional_topping


class Doordelivery(Pizzaservice):

    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__delivery_charge = None
        self.__distance_in_kms = distance_in_kms

    def validate_distance_in_kms(self):
        if self.__distance_in_kms >= 1 and self.__distance_in_kms <= 10:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if not self.pizza_cost == -1:
                if self.__distance_in_kms <= 5:
                    self.__delivery_charge = self.__distance_in_kms * 5
                else:
                    self.__delivery_charge = 25 + \
                        (self.__distance_in_kms - 5) * 7
                self.pizza_cost += self.__delivery_charge
        else:
            self.pizza_cost = -1

    def get_delivery_charge(self):
        return self.__delivery_charge

    def get_distance_in_kms(self):
        return self.__distance_in_kms
