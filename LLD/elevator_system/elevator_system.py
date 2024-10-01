from enum import Enum, auto
from abc import ABC, abstractmethod

import time
import threading
from heapq import heappop, heappush


class State(Enum):
    IDLE = auto()
    MOVING = auto()

class Direction(Enum):
    UP = auto()
    DOWN = auto()


class ElevatorButtonPanel:
    def __init__(self, elevator_car: 'ElevatorCar'):
        self.car = elevator_car

    def press(self, floor: int):
        if not self.car.serviceable:
            print('Elevator is not serviceable!')
            return False

        if 0 <= floor <= self.car.floors:
            # 1. Add request to move to that floor
            self.car.handler.inside_request(floor)
        else:
            print('Unknown floor value')


class ElevatorRequestHandler:
    def __init__(self, elevator_car: 'ElevatorCar'):
        self.elevator = elevator_car
        self.request1 = []
        self.request2 = []
        self.request3 = []

    @staticmethod
    def get_direction(source_floor: int, target_floor: int):
        return Direction.UP if target_floor >= source_floor else Direction.DOWN

    @staticmethod
    def add_request(request, floor, direction):
        heappush(request,(floor if direction == Direction.UP else -floor, direction))

    def execute(self):
        if self.request1:
            f, d = heappop(self.request1)
            print(f'Elevator Car {self.elevator.id} came {d.name} to floor {f}')

        if not self.request1 and self.request2:
            self.request2 = self.request1
            self.request3 = self.request2

    def outside_request(self, floor: int, direction: Direction):
        if not self.elevator.is_moving():
            if self.elevator.current_floor < floor:
                self.add_request(self.request1, floor, direction)
            else:
                self.add_request(self.request1, floor, direction)

        if self.elevator.direction == Direction.UP == direction:
            if self.elevator.current_floor < floor:
                self.add_request(self.request1, floor, direction)
            else:
                self.add_request(self.request3, floor, direction)

        if self.elevator.direction == Direction.DOWN == direction:
            if self.elevator.current_floor < floor:
                self.add_request(self.request3, floor, direction)
            else:
                self.add_request(self.request1, floor, direction)

        if self.elevator.direction != direction:
            self.add_request(self.request2, floor, direction)


    def inside_request(self, floor: int):
        if self.elevator.direction == Direction.UP:
            if self.elevator.current_floor < floor:
                self.add_request(self.request1, floor, Direction.UP)
            else:
                self.add_request(self.request2, floor, Direction.DOWN)

        else:
            if self.elevator.current_floor > floor:
                self.add_request(self.request1, floor, Direction.DOWN)
            else:
                self.add_request(self.request2, floor, Direction.UP)



class ElevatorCar:
    def __init__(self, id: int, floors: int):
        self.id = id
        self.floors = floors
        self.current_floor = 0
        self.state: State = State.IDLE
        self.direction: Direction = Direction.UP
        self.button_panel: ElevatorButtonPanel = ElevatorButtonPanel(self)
        self.serviceable = False
        # Manager to move the elevator
        self.handler = ElevatorRequestHandler(self)

    def is_moving(self):
        return self.state == State.MOVING

    def set_serviceable(self):
        self.serviceable = True

    def set_unserviceable(self):
        self.serviceable = False

    def run(self):
        while self.serviceable:
            self.handler.execute()
            time.sleep(1)

    def start(self):
        t = threading.Thread(target=self.run())
        t.join()


class ElevatorSelectionStrategy(ABC):
    def __init__(self, elevator_system: 'ElevatorSystem'):
        self.system = elevator_system

    @staticmethod
    def service_turn(elevator: ElevatorCar, floor: int, direction: Direction) -> int:
        if not elevator.is_moving():
            return abs(floor-elevator.current_floor)
        if elevator.direction == direction:
            if elevator.current_floor < floor:
                return floor - elevator.current_floor
            else:
                return 2*elevator.floors-(elevator.current_floor-floor)
        return 2*elevator.floors-elevator.current_floor-floor

    @abstractmethod
    def select(self, floor: int, direction: Direction) -> ElevatorCar:
        pass


class DefaultSelectionStrategy(ElevatorSelectionStrategy):
    def select(self, floor: int, direction: Direction) -> ElevatorCar:
        selected = min(self.system.elevators, key=lambda e: self.service_turn(e, floor, direction))
        return selected


class SelectionStrategyEnum(Enum):
    DEFAULT = auto()

class SelectionStrategyFactory:
    strategy_map = {
        SelectionStrategyEnum.DEFAULT: DefaultSelectionStrategy
    }
    @staticmethod
    def get_selection_strategy(strategy: SelectionStrategyEnum, elevator_system: 'ElevatorSystem'):
        if strategy in SelectionStrategyFactory.strategy_map:
            return SelectionStrategyFactory.strategy_map[strategy](elevator_system)
        raise ValueError('Invalid strategy found!')


class OutsideButtonPanel:
    def __init__(self, elevator_system: 'ElevatorSystem', strategy: SelectionStrategyEnum):
        self.system = elevator_system
        self.strategy = SelectionStrategyFactory.get_selection_strategy(strategy, self.system)

    def call(self, floor: int,  direction: Direction):
        # 1. Choose the right elevator
        elevator = self.strategy.select(floor, direction)
        # 2. Request the elevator at that floor
        elevator.handler.outside_request(floor, direction)


class ElevatorSystem:
    def __init__(self, floors: int, num_of_cars: int):
        self.floors = floors
        self.elevators = [ElevatorCar(i, floors) for i in range(num_of_cars)]
        self.button_panel: OutsideButtonPanel = OutsideButtonPanel(self, SelectionStrategyEnum.DEFAULT)


    def start(self):
        for elevator in self.elevators:
            elevator.set_serviceable()
            elevator.start()

    def stop(self):
        for elevator in self.elevators:
            elevator.set_unserviceable()


if __name__ == '__main__':
    elevator_system = ElevatorSystem(5, 3)
    elevator_system.start()