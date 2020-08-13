class Train:

    def __init__(self,train_name,source,destination,passenger_capacity_per_compartment,passenger_goods_ratio):
        self.__train_name = train_name
        self.__source = source
        self.__destination = destination
        self.__passenger_capacity_per_compartment = passenger_capacity_per_compartment
        self.__passenger_goods_ratio = passenger_goods_ratio

    def get_train_name(self):
        return self.__train_name

    def get_source(self):
        return self.__source
    
    def get_destination(self):
        return self.__destination
    
    def get_passenger_capacity_per_compartment(self):
        return self.__passenger_capacity_per_compartment

    def get_passenger_goods_ratio(self):
        return self.__passenger_goods_ratio

    def __str__(self):
        return ""