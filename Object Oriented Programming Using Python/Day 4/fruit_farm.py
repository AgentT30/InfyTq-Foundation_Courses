class FruitInfo:

    __fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    __fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        for i in range(len(FruitInfo.__fruit_name_list)):
            if fruit_name == FruitInfo.__fruit_name_list[i]:
                return FruitInfo.__fruit_price_list[i]
        return -1

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list


class Purchase:

    __counter = 101

    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = None
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        fruit_price = FruitInfo.get_fruit_price(self.__fruit_name)
        if not fruit_price == -1:
            if fruit_price == max(FruitInfo.get_fruit_price_list()) and self.__quantity > 1:
                fruit_price *= self.__quantity
                fruit_price -= fruit_price * 0.02
            elif fruit_price == min(FruitInfo.get_fruit_price_list()) and self.__quantity >= 5:
                fruit_price *= self.__quantity
                fruit_price -= fruit_price * 0.05
            else:
                fruit_price *= self.__quantity

            if self.__customer.get_cust_type() == "wholesale":
                fruit_price -= fruit_price * 0.1
            self.__purchase_id = "P" + str(Purchase.__counter)
            Purchase.__counter += 1
            return fruit_price
        else:
            return -1


class Customer:

    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name

    def get_cust_type(self):
        return self.__cust_type
