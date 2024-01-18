from abc import ABC, abstractmethod


# creating Transport class which is product of the factory method
class Transport(ABC):
    def ship(self):
        pass


class RailTransport(Transport):
    def ship(self):
        print('Transporting through Railways')


class AirTransport(Transport):
    def ship(self):
        print('Transporting through Airways')


class SeaTransport(Transport):
    def ship(self):
        print('Transporting through Sea')


# creating Logistic class and concrete classes which will implement the factory method
class Logistic(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def start(self):
        transport = self.create_transport()
        transport.ship()


class RailLogistic(Logistic):
    def create_transport(self):
        return RailTransport()


class AirLogistic(Logistic):
    def create_transport(self):
        return AirTransport()


class SeaLogistic(Logistic):
    def create_transport(self):
        return SeaTransport()


if __name__ == '__main__':
    logistic = RailLogistic()
    logistic.start()

    logistic = AirLogistic()
    logistic.start()

    logistic = SeaLogistic()
    logistic.start()
