from abc import ABCMeta, abstractmethod


class DirectToHomeService(ABCMeta):

    __counter = 101

    def __init__(self, consumer_name):
        self.__consumer_name = consumer_name
        self.__consumer_number = DirectToHomeService.__counter
        DirectToHomeService.__counter += 1

    def get_consumer_number(self):
        return self.__consumer_number

    def get_consumer_name(self):
        return self.__consumer_name

    @abstractmethod
    def calculate_monthly_rent(self):
        pass


class BasePackage(DirectToHomeService):

    def __init__(self, consumer_name, base_pack_name, subscription_period):
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period
        super().__init__(consumer_name)

    def get_base_pack_name(self):
        return self.__base_pack_name

    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        pack_name = self.get_base_pack_name()
        if pack_name.lower() == "silver" or pack_name.lower() == "gold" or pack_name.lower() == "platinum":
            print("Valid")
        else:
            self.__base_pack_name = "Silver"
            print("Base package name is incorrect, set to Silver")

    def calculate_monthly_rent(self):
        if self.get_subscription_period() >= 1 and self.get_subscription_period() <= 24:
            self.validate_base_pack_name()
            monthly_rent = 0
            dicount = 0
            if self.get_base_pack_name().lower() == "silver":
                monthly_rent = 350
            elif self.get_base_pack_name().lower() == "gold":
                monthly_rent = 440
            else:
                monthly_rent = 560

            if self.get_subscription_period() > 12 and self.get_base_pack_name().lower() == "silver":
                discount = 350
            elif self.get_subscription_period() > 12 and self.get_base_pack_name().lower() == "gold":
                discount = 440
            elif self.get_subscription_period() > 12 and self.get_base_pack_name().lower() == "platinum":
                discount = 560

            final_monthly_rent = (
                (monthly_rent * self.get_subscription_period()) - dicount) / self.get_subscription_period()
            return final_monthly_rent
        else:
            return -1
