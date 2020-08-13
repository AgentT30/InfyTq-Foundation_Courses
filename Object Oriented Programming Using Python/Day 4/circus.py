class Rider:

    def __init__(self, trained_status, experience):
        self.__trained_status = trained_status
        self.__experience = experience

    def rides_vehicle(self):
        return "Rides Vehicle!"


class BikeRider(Rider):

    def __init__(self, trained_status, experience, race_license):
        self.__trained_status = trained_status
        self.__experience = experience
        self.__race_license = race_license

    def rides_in_dome(self):
        return "Rides in Dome!"


class CycleRider(Rider):

    def rides_blindfolded(self):
        return "Rides blindfolded!"
