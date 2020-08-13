class Ticket:
    counter = 0

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = None
        self.__source = source
        self.__destination = destination

    def validate_source_destination(self):
        if self.__source.upper() == "DELHI":
            if self.__destination.upper() == "MUMBAI" or self.__destination.upper() == "CHENNAI" or self.__destination.upper() == "PUNE" or self.__destination.upper() == "KOLKATA":
                return True
            else:
                return False
        else:
            return False

    def generate_ticket(self):
        if self.validate_source_destination():
            source = self.get_source()
            dest = self.get_destination()
            Ticket.counter += 1
            self.__ticket_id = source[0] + \
                dest[0] + str(Ticket.counter).zfill(2)
        else:
            self.__ticket_id = None

    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination
