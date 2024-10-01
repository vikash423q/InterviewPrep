# A TheatreManager class will be responsible for adding/removing screenings
# TheatreManager will shows all the screening available to book, select screening and show all the seats to book
# Will have classes like Movie, Seat
# Seat will have Enum - Regular, Executive which will decide seat price
# Screening will have movie, seats and time
# User will be able to book the seats, and a MovieTicket will be provided

import uuid
from typing import List, Dict, Union, Set
from enum import Enum, auto
from datetime import datetime, date
from termcolor import colored
from threading import Lock


class SeatType(Enum):
    REGULAR = auto()
    EXECUTIVE = auto()


class Theatre:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name


class Movie:
    def __init__(self, name: str):
        self.name = name


class Seat:
    def __init__(self, row: int, col: int, seat_type: SeatType):
        self.name = f'{row}:{col}'
        self.type: SeatType = seat_type

    def __repr__(self):
        return self.name


class Screen:
    def __init__(self, number: int):
        self.number = number
        self.seats: List[List[Seat]] = []
        self.rows = 0
        self.cols = 0

    def initialize_seats(self, rows: int, cols: int, row_type_map: Dict[int, SeatType]):
        for row in range(1, rows + 1):
            row_seats = []
            for col in range(1, cols + 1):
                row_seats.append(Seat(row, col, row_type_map.get(row, SeatType.REGULAR)))
            self.seats.append(row_seats)
        self.rows = rows
        self.cols = cols

    def get_seat_by_name(self, seat_name: str):
        for row in self.seats:
            for seat in row:
                if seat.name == seat_name:
                    return seat
        return


class Screening:
    def __init__(self, movie: Movie, screen: Screen, time: datetime):
        self.movie = movie
        self.screen = screen
        self.time = time
        self.booked: Set[str] = set()


    def is_available(self, seat: Seat):
        return seat.name not in self.booked


    def is_housefull(self):
        return len(self.booked) == len(self.screen.seats[0])*len(self.screen.seats)


    def book(self, seat: Seat):
        if seat.name in self.booked:
            raise Exception(f'This seat {seat} is already booked!')
        self.booked.add(seat.name)

    def show(self):
        print(f'\n---------- Showing Screen {self.screen.number} Layout  -------------\n')
        for row in reversed(self.screen.seats):
            print(row[0].type.name.rjust(12), end=" ")
            print("Rs.", FareCalculator(row[0], self).calculate(), end=" ")
            print("\t".join([colored(f"[{st.name}]", 'green') if self.is_available(st) else f"[{st.name}]" for st in row]))
        print()


class FareStrategy:
    def calculate(self, seat: Seat, screening: Screening) -> float:
        raise NotImplementedError

class DefaultFareStrategy(FareStrategy):
    def calculate(self, seat: Seat, screening: Screening) -> float:
        if screening.time.hour <= 12:
            price = 150
        elif screening.time.hour <= 18:
            price = 180
        else:
            price = 220

        if seat.type == SeatType.EXECUTIVE:
            price += 100
        return price

class FareCalculator:
    def __init__(self, seat: Seat, screening: Screening, strategy: FareStrategy = DefaultFareStrategy()):
        self.seat = seat
        self.screening = screening
        self.strategy = strategy
        self.gst = 0.18

    def calculate(self) -> float:
        return self.strategy.calculate(self.seat, self.screening)

    def calculate_total(self):
        return round(self.calculate() * (1 + self.gst), 2)



class MovieTicket:
    def __init__(self,seat: Seat, screening: Screening):
        self.seat = seat
        self.screening = screening
        self.price = FareCalculator(seat, screening).calculate_total()

    def __repr__(self):
        return f"\nYour movie ticket\n------------\nMovie: {self.screening.movie.name}" \
               f"\nFrom: {self.screening.time}\nSeat(s): {self.seat}\nTicket Price: {self.price}\n-------------"


class TheatreManager:
    _instance = {}

    def __new__(cls, theatre: Theatre):
        if theatre.id not in cls._instance:
            cls._instance[theatre.id] = super(TheatreManager, cls).__new__(cls)
        return cls._instance[theatre.id]

    def __init__(self, theatre: Theatre):
        self.theatre = theatre
        self.screens: List[Screen] = []
        self.screenings: List[Screening] = []
        self.lock = Lock()

    def add_screen(self, screen: Screen):
        for sc in self.screens:
            if sc.number == screen.number:
                raise Exception('Multiple screens cannot have same screen number!')
        self.screens.append(screen)

    def add_screening(self, screening: Screening):
        self.screenings.append(screening)

    def show_screenings(self, dt: date = None, movie: str = None):
        filtered = self.screenings
        if dt:
            filtered = [sc for sc in filtered if sc.time.date() == dt]
        if movie:
            filtered = [sc for sc in filtered if sc.movie.name == movie]

        filtered.sort(key=lambda s: s.time)

        for i, sc in enumerate(filtered):
            print(i+1, sc.time, '----->', sc.movie.name)

        n = input('\n\tSelect screening: ')
        selected = filtered[int(n)-1]
        selected.show()


    def book_ticket(self, screening: Screening, seat_name: str) -> Union[MovieTicket]:
        with self.lock:
            seat = screening.screen.get_seat_by_name(seat_name)
            if not seat:
                raise Exception("Invalid seat provided!")

            if screening.is_available(seat):
                screening.book(seat)
                if not screening.is_available(seat):
                    screening.show()
                    return MovieTicket(seat, screening)
                raise Exception('Error: Ticket not booked!')
            else:
                print(f'Error: Seat {seat} not available!')


class TheatreController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(TheatreController, cls).__new__(cls)
        return cls._instance


    def __init__(self):
        self.theatres = []

    def add_theatre(self, theatre: Theatre):
        self.theatres.append(theatre)

    def get_theatre_manager(self, theatre_name: str) -> TheatreManager:
        for theatre in self.theatres:
            if theatre.name == theatre_name:
                return TheatreManager(theatre)
        raise Exception(f'No theatre with name {theatre_name} found!')

if __name__ == '__main__':
    theatre_controller1 = TheatreController()
    theatre_controller1.add_theatre(Theatre('PVR Inox'))

    theatre_manager = theatre_controller1.get_theatre_manager('PVR Inox')

    # Creating Screen and Initializing seats
    screen1 = Screen(1)
    screen1.initialize_seats(5, 5, {5: SeatType.EXECUTIVE})
    screen2 = Screen(2)
    screen2.initialize_seats(5, 5, {4: SeatType.EXECUTIVE, 5: SeatType.EXECUTIVE})
    screen3 = Screen(3)
    screen3.initialize_seats(5, 5, {4: SeatType.EXECUTIVE, 5: SeatType.EXECUTIVE})

    # Adding Screen to theatre manager
    theatre_manager.add_screen(screen1)
    theatre_manager.add_screen(screen2)
    theatre_manager.add_screen(screen3)

    # Creating movies and screenings
    movie1 = Movie('TOP GUN: Maverick')
    movie2 = Movie('The Matrix')

    screening1 = Screening(movie1, screen1, datetime(2024, 9, 30, 10, 30))
    screening2 = Screening(movie1, screen1, datetime(2024, 9, 30, 13, 30))

    screening3 = Screening(movie2, screen2, datetime(2024, 9, 30, 13, 30))
    screening4 = Screening(movie2, screen2, datetime(2024, 9, 30, 22, 00))

    # Adding screenings to theatre manager
    theatre_manager.add_screening(screening1)
    theatre_manager.add_screening(screening2)
    theatre_manager.add_screening(screening3)
    theatre_manager.add_screening(screening4)


    # Testing -----
    # theatre_manager.show_screenings()

    ticket = theatre_manager.book_ticket(screening3, "1:1")
    print(ticket)

    ticket2 = theatre_manager.book_ticket(screening1, "1:1")
    print(ticket2)



