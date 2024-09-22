import time

from threading import Thread
from enum import Enum, auto
from heapq import *


class Direction(Enum):
    UP = auto()
    DOWN = auto()


class State(Enum):
    IDLE = auto()
    MOVING = auto()
    STOPPED = auto()


class ElevatorSystem:
    def __init__(self,):
        self.elevators = []

    def add_elevator(self, num_of_floor):
        self.elevators.append(ElevatorHandler(num_of_floor))


class ElevatorHandler:
    def __init__(self, num_floor: int):
        self.elevator = Elevator(num_floor)

    def call_to_floor(self, floor: int, direction: Direction):
        print(f'\nCALL requested at {floor} to go {"UP" if direction == Direction.UP else "DOWN"}\n')
        self.elevator.add_request(floor, direction)

    def stop_at_floor(self, floor: int):
        if self.elevator.state == State.IDLE:
            print(f'\nSTOP requested at floor {floor}\n')
            self.elevator.add_request(floor, Direction.UP if floor > self.elevator.current_floor else Direction.DOWN)
        elif self.elevator.direction == Direction.UP and floor > self.elevator.current_floor:
            print(f'\nSTOP requested at floor {floor}\n')
            self.elevator.add_request(floor, Direction.UP)
        elif self.elevator.direction == Direction.DOWN and floor < self.elevator.current_floor:
            print(f'\nSTOP requested at floor {floor}\n')
            self.elevator.add_request(-floor, Direction.DOWN)

    def start_elevator(self):
        self.t = Thread(target=self.elevator.run)
        self.t.start()
        # self.t.join()

    def stop_elevator(self):
        self.elevator.stop()

    def wait(self):
        self.t.join()


class Elevator:
    def __init__(self, num_floors: int, current_floor: int = 0):
        self.num_floors = num_floors
        self.current_floor = current_floor
        self.state = State.IDLE
        self.direction = Direction.UP
        self.primary_requests = []
        self.secondary_requests = []
        self.tertiary_requests = []

    def stop(self):
        self.state = State.STOPPED
        print('Elevator is stopped!')

    def add_request(self, floor: int, direction: Direction):
        if floor < 0 or floor >= self.num_floors:
            print(f'Invalid floor {floor} requested! Allowed range -> [0, {self.num_floors}]')
            return
        if self.direction == direction == Direction.UP and floor >= self.current_floor:
            heappush(self.primary_requests, (floor, direction))

        elif self.direction == direction == Direction.DOWN and floor <= self.current_floor:
            heappush(self.primary_requests, (-floor, direction))

        elif self.direction != direction:
            heappush(self.secondary_requests, (floor if direction == Direction.UP else -floor, direction))

        elif self.direction == direction == Direction.UP and floor < self.current_floor:
            heappush(self.tertiary_requests, (floor, direction))

        elif self.direction == direction == Direction.DOWN and floor > self.current_floor:
            heappush(self.tertiary_requests, (-floor, direction))

    def run(self):
        self.state = State.IDLE
        while self.state != State.STOPPED:
            if not self.primary_requests:
                self.state = State.IDLE

            if not self.primary_requests and self.secondary_requests:
                self.primary_requests = self.secondary_requests
                self.secondary_requests = self.tertiary_requests
                self.tertiary_requests = []

            if self.primary_requests:
                self.state = State.MOVING
                floor, direction = self.primary_requests[0]
                floor = abs(floor)

                if floor == self.current_floor:
                    print(f'Opening door at floor {floor}')
                    heappop(self.primary_requests)
                else:
                    self.direction = Direction.UP if floor > self.current_floor else Direction.DOWN
                    print(f'Moving {"UP" if self.direction == Direction.UP else "DOWN"} from floor {self.current_floor} to floor {floor}')

                    if self.direction == Direction.UP:
                        self.current_floor += 1
                    elif self.direction == Direction.DOWN:
                        self.current_floor -= 1

            time.sleep(1)


if __name__ == '__main__':
    elevator_system = ElevatorHandler(20)
    elevator_system.start_elevator()

    time.sleep(2)
    elevator_system.call_to_floor(3, Direction.UP)
    elevator_system.call_to_floor(45, Direction.UP)

    time.sleep(2)
    elevator_system.call_to_floor(1, Direction.UP)

    time.sleep(5)
    elevator_system.call_to_floor(2, Direction.DOWN)
    time.sleep(5)
    elevator_system.stop_at_floor(9)
    elevator_system.stop_elevator()
    elevator_system.wait()



