# Parking lot will have a parking manager
# supports park and unpark vehicle
# search vehicle with vehicle number
# will have ParkingArea on ParkingFloor
# ParkingArea will have multiple ParkingSpot
# ParkingSpot will have compact, regular, large

import math
from typing import Dict, List, Union
from abc import ABC, abstractmethod
from enum import Enum, auto
from datetime import datetime, timedelta
from termcolor import colored
from threading import Lock


class Size(Enum):
    COMPACT = 1
    REGULAR = 2
    LARGE = 3


class ParkingStrategyEnum(Enum):
    VIP = auto()
    FCFS = auto()
    BEST_FIT = auto()



class Vehicle:
    def __init__(self, plate_number: str, vip: bool = False):
        self.plate_number = plate_number
        self.size = Size.REGULAR
        self.VIP = vip

class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = Size.REGULAR

class Bike(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = Size.COMPACT

class Truck(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = Size.LARGE


class ParkingTicket:
    def __init__(self, floor: int, spot: 'ParkingSpot', vehicle: Vehicle):
        self.spot = spot
        self.floor = floor
        self.vehicle = vehicle
        self.parked_at = datetime.now()
        self.base_price = 10

    def get_fare(self) -> float:
        delta = datetime.now() - self.parked_at
        hours = math.ceil(delta.total_seconds())
        return self.spot.size.value*self.base_price*hours


class ParkingSpot:
    def __init__(self, row: int, col: int, size: Size):
        self.size = size
        self.row = row
        self.col = col
        self.vehicle: Union[Vehicle, None] = None

    def park(self, vehicle: Vehicle):
        if vehicle.size.value > self.size.value:
            return False
        self.vehicle = vehicle
        return True

    def un_park(self):
        if self.vehicle:
            self.vehicle = None
            return True
        return False

    def fit(self, vehicle: Vehicle):
        return self.available() and self.size.value >= vehicle.size.value

    def available(self) -> bool:
        return not bool(self.vehicle)

    def __repr__(self):
        return f"{self.row}|{self.col}"


class ParkingSpace:
    def __init__(self, floor: int, row: int, col: int, size: Size):
        self.row = row
        self.col = col
        self.size = size
        self.floor = floor
        self.spots: List[List[ParkingSpot]] = [[ParkingSpot(r, c, size) for c in range(col)] for r in range(row)]

    def num_of_spot_available(self, vehicle: Vehicle) -> int:
        return sum([self.spots[r][c].fit(vehicle) for r in range(self.row) for c in range(self.col)])


    def park(self, row: int, col: int, vehicle: Vehicle):
        if 0 <= row < self.row and 0 <= col < self.col:
            spot = self.spots[row][col]
            return spot.park(vehicle)
        raise ValueError("Unknown spot")


    def un_park(self, row: int, col: int):
        if 0 <= row < self.row and 0 <= col < self.col:
            spot = self.spots[row][col]
            return spot.un_park()
        raise ValueError("Unknown spot")

    def __repr__(self):
        rows = [f"------------ Parking Space for floor {self.floor} --------------"]
        for r in range(self.row):
            lines = []
            for c in range(self.col):
                spot = self.spots[r][c]
                if spot.available():
                    lines.append(f'  [{r}:{c}:{"A"}]'.ljust(8))
                else:
                    lines.append(colored(f'  [{r}:{c}:{spot.vehicle.plate_number}]'.ljust(8), 'red'))

            rows.append("\t".join(lines))
        return "\n".join(rows)


class ParkingStrategyFactory:
    @staticmethod
    def get_strategy(vehicle: Vehicle, floor_parking: dict, strategy_type: ParkingStrategyEnum):
        if vehicle.VIP or strategy_type == ParkingStrategyEnum.VIP:
            return VIPParkingStrategy(floor_parking, vehicle)
        elif strategy_type == ParkingStrategyEnum.FCFS:
            return FCFSParkingStrategy(floor_parking, vehicle)
        elif strategy_type == ParkingStrategyEnum.BEST_FIT:
            return BestFitParkingStrategy(floor_parking, vehicle)
        raise ValueError('Unknown strategy')


class ParkingStrategy(ABC):
    def __init__(self, floor_parking: dict, vehicle: Vehicle):
        self.vehicle = vehicle
        self.floor_parking: Dict[int, ParkingSpace] = floor_parking

    @abstractmethod
    def park(self) -> Union[ParkingTicket, None]:
        pass


class FCFSParkingStrategy(ParkingStrategy):
    def park(self) -> Union[ParkingTicket, None]:
        for floor, parking_space in self.floor_parking.items():
            for row in parking_space.spots:
                for spot in row:
                    if spot.fit(self.vehicle):
                        parking_space.park(spot.row, spot.col, self.vehicle)
                        return ParkingTicket(floor, spot, self.vehicle)
        return None


class BestFitParkingStrategy(ParkingStrategy):
    def park(self) -> Union[ParkingTicket, None]:
        floor_parking_pair = list(self.floor_parking.items())
        floor_parking_pair.sort(key=lambda x: x[1].size.value)
        for floor, parking_space in floor_parking_pair:
            for row in parking_space.spots:
                for spot in row:
                    if spot.fit(self.vehicle):
                        parking_space.park(spot.row, spot.col, self.vehicle)
                        return ParkingTicket(floor, spot, self.vehicle)
        return None


class VIPParkingStrategy(ParkingStrategy):
    def park(self) -> Union[ParkingTicket, None]:
        for floor, parking_space in self.floor_parking.items():
            if parking_space.size == Size.LARGE:
                for row in parking_space.spots:
                    for spot in row:
                        if spot.fit(self.vehicle):
                            parking_space.park(spot.row, spot.col, self.vehicle)
                            return ParkingTicket(floor, spot, self.vehicle)

        for floor, parking_space in self.floor_parking.items():
            for row in parking_space.spots:
                for spot in row:
                    if spot.fit(self.vehicle):
                        parking_space.park(spot.row, spot.col, self.vehicle)
                        return ParkingTicket(floor, spot, self.vehicle)
        return None


class ParkingManager:
    def __init__(self, floors: int):
        self.floors = floors
        self.floor_parking: Dict[int, ParkingSpace] = {}
        self.parked_vehicle_map: Dict[str, ParkingTicket] = {}
        self.lock = Lock()


    def add_parking_space(self, floor: int, row: int, col: int, size: Size):
        if 0 <= floor <= self.floors:
            self.floor_parking[floor] = ParkingSpace(floor, row, col, size)

    def park(self, vehicle: Vehicle, parking_strategy = ParkingStrategyEnum.FCFS):
        if vehicle.plate_number in self.parked_vehicle_map:
            raise Exception('Vehicle already parked!')

        with self.lock:
            strategy = ParkingStrategyFactory.get_strategy(vehicle, self.floor_parking, parking_strategy)
            ticket = strategy.park()
            if not ticket:
                return None

            print(f'Vehicle {vehicle.plate_number} is parked at Floor: {ticket.floor} At Spot: {ticket.spot}')
            self.parked_vehicle_map[vehicle.plate_number] = ticket
            return ticket


    def un_park(self, vehicle: Vehicle):
        with self.lock:
            if vehicle.plate_number in self.parked_vehicle_map:
                ticket = self.parked_vehicle_map[vehicle.plate_number]
                parking_space = self.floor_parking[ticket.floor]
                parking_space.un_park(ticket.spot.row, ticket.spot.col)
                print(f'Vehicle {vehicle.plate_number} unparked. Your bill is {ticket.get_fare()}')
                del self.parked_vehicle_map[vehicle.plate_number]


    def num_of_available_space(self, vehicle: Vehicle):
        return sum(parking_space.num_of_spot_available(vehicle) for f, parking_space in self.floor_parking.items())


    def show(self):
        for floor in range(self.floors-1, -1, -1):
            if floor not in self.floor_parking:
                continue
            print(self.floor_parking[floor])



if __name__ == '__main__':
    parking_manager = ParkingManager(5)
    parking_manager.add_parking_space(0, 5, 5, Size.LARGE)
    parking_manager.add_parking_space(1, 5, 5, Size.COMPACT)
    parking_manager.add_parking_space(4, 5, 5, Size.REGULAR)

    print(parking_manager.num_of_available_space(Bike('XYZ')))
    print(parking_manager.num_of_available_space(Car('XYZ123')))
    print(parking_manager.num_of_available_space(Truck('TXYZ')))

    parking_manager.park(Car('ABC'), ParkingStrategyEnum.BEST_FIT)
    parking_manager.park(Car('BMW'), ParkingStrategyEnum.VIP)
    parking_manager.park(Car('BMWX'), ParkingStrategyEnum.BEST_FIT)

    parking_manager.show()


    import time
    time.sleep(2)
    parking_manager.un_park(Car('BMW'))
    parking_manager.un_park(Car('BMWX'))
    time.sleep(1)
    parking_manager.un_park(Car('ABC'))