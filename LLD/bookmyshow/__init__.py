from typing import List
from threading import Thread

from enum import Enum, auto
from datetime import datetime, timedelta


#   user should be able to select from a list of shows
#   user should be able to select a list of venues
#   user should be able to select a screening time at the venue
#   user should be able to list the available and non-available seats
#   user should be able to checkout the desired seat which will be locked for a specific duration, and other users can't choose the seat
#   user should be able to finalize the seat.


class SeatType(Enum):
    REGULAR = auto()
    EXECUTIVE = auto()


class Show:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration


class Seat:
    def __init__(self, number: str, price: int, seat_type: SeatType = SeatType.REGULAR, available: bool = True):
        self.number = number
        self.seat_type = seat_type
        self.price = price
        self.available = available


class Screening:
    def __init__(self, show: Show, start_time: datetime):
        self.show = show
        self.start_time = start_time
        self.seats = []

    def add_seats(self, start_row: int, end_row: int, col: int, price: int, seat_type=SeatType.REGULAR):
        self.seats += [Seat(f'{chr(r + ord("A"))}{c+1}', price, seat_type) for r in range(start_row, end_row) for c in range(col)]


class Venue:
    def __init__(self, name, location: str = ''):
        self.name = name
        self.location = location
        self.screenings = []

    def add_screening(self, show: Show,  start_time: datetime, prices: tuple, row: int = 5, col: int = 5):
        sc = Screening(show, start_time)
        sc.add_seats(0, row-2,  col, prices[0])
        sc.add_seats(row-2, row, col, prices[1], SeatType.EXECUTIVE)
        self.screenings.append(sc)


class BookingSystem:
    def __init__(self, shows: List[Show], venues: List[Venue]):
        self.shows = shows
        self.venues = venues
        self.ttl_cache = {}

    def ttl_check(self):
        t = datetime.now()

        remove_keys = []
        for key in self.ttl_cache:
            if t > self.ttl_cache[key]:
                remove_keys.append(key)

        for k in remove_keys:
            del self.ttl_cache[k]

    def confirm_booking(self, key):
        if key in self.ttl_cache:
            return Exception('Seat not available for booking!')

        v, s, time, num = key
        for venue in self.venues:
            if venue.name == v:
                for sc in venue.screenings:
                    if sc.start_time == time and sc.show.name == s:
                        for seat in sc.seats:
                            if not seat.available:
                                return Exception('Seat is already booked!')
                            if seat.number == num:
                                seat.available = False

        if key in self.ttl_cache:
            del self.ttl_cache[key]

    @staticmethod
    def wait_for_input(cls):
        while True:
            try:
                return cls(input())
            except ValueError:
                print('Invalid value. Try again')

    def select_show(self):
        for i, show in enumerate(self.shows, 1):
            print(f'{i} {show.name} -: duration -> {show.duration}')

        print('Type show number to select. Type 0 to exit')
        idx = self.wait_for_input(int)
        if idx == 0:
            exit()

        if 0 < idx <= len(self.shows):
            return self.shows[idx-1]

    def select_venue(self, show):
        filtered_venues = []

        for venue in self.venues:
            for sc in venue.screenings:
                if sc.show == show:
                    filtered_venues.append(venue)
                    break

        for i, venue in enumerate(filtered_venues, 1):
            print(f'{i} {venue.name}')
            for sc in venue.screenings:
                if sc.show == show:
                    print(f'\tScreening time {sc.start_time}')

        print('Type venue number to select. Type 0 to exit')
        idx = self.wait_for_input(int)
        if idx == 0:
            exit()

        if 0 < idx <= len(filtered_venues):
            return filtered_venues[idx-1]

    def select_screening(self, venue: Venue, show: Show) -> Screening:
        filtered_sc = [sc for sc in venue.screenings if sc.show == show]
        for i, sc in enumerate(filtered_sc, 1):
            print(f'{i} {sc.show.name} start_time -> {sc.start_time}')

        print('Type screening number to select. Type 0 to exit')
        idx = self.wait_for_input(int)
        if idx == 0:
            exit()

        if 0 < idx <= len(filtered_sc):
            return filtered_sc[idx-1]

    def select_seat(self, venue, screening: Screening):
        last = 'NA'
        name_seat_map = {st.number: st for st in screening.seats}
        for seat in screening.seats:
            if last[:1] != seat.number[:1]:
                print()
            key = (venue.name, screening.show.name, screening.start_time, seat.number)
            available = "NA" if key in self.ttl_cache else ('A' if seat.available else 'NA')
            print(f'\t\'{seat.number}:{available}\'', end='  ')
            last = seat.number

        print('\nType seat number to select. Type 0 to exit')
        seat = None

        while seat is None:
            val = self.wait_for_input(str)
            if val == "0":
                exit()

            seat = name_seat_map.get(val.upper())
            if not seat:
                print('Invalid seat name. Try again!')
        return seat

    def process_with_screening(self, show, venue, screening):
        self.ttl_check()
        seat = self.select_seat(venue, screening)
        key = (venue.name, show.name, screening.start_time, seat.number)

        while key in self.ttl_cache:
            print(f'Seat is not available! Try again!')
            self.process_with_screening(show, venue, screening)

        self.ttl_cache[key] = datetime.now() + timedelta(minutes=10)
        n = input(f'Confirm Payment of Rs.{seat.price}? Y/N')

        if n.upper() == 'Y':
            self.confirm_booking(key)
            print(f'Ticket Confirmed! Venue: {key[0]} Seat: {key[3]} Time: {key[2]}')
            print()
            self.process()
        elif n.upper() == 'N':
            print()
            print('Starting again..')
            self.process_with_screening(show, venue, screening)

    def process(self):
        show = self.select_show()
        venue = self.select_venue(show)
        screening = self.select_screening(venue, show)

        self.process_with_screening(show, venue, screening)


if __name__ == '__main__':
    shows = [Show('Oppenheimer', 180), Show('12th Fail', 150), Show('Tiger 3', 140)]
    venues = [Venue('Forum Mall'), Venue('Meenakshi Mall'), Venue('Cinepolis')]

    today = datetime.today().replace(minute=0, second=0, microsecond=0)
    # adding screenings
    venues[0].add_screening(shows[0], today.replace(hour=9), prices=(250, 400))
    venues[0].add_screening(shows[0], today.replace(hour=12), prices=(250, 400))
    venues[0].add_screening(shows[1], today.replace(hour=13), prices=(180, 320))

    venues[1].add_screening(shows[0], today.replace(hour=8), prices=(280, 420))
    venues[1].add_screening(shows[1], today.replace(hour=11), prices=(160, 300))
    venues[1].add_screening(shows[2], today.replace(hour=15), prices=(190, 320))

    venues[2].add_screening(shows[0], today.replace(hour=9), prices=(150, 300))
    venues[2].add_screening(shows[2], today.replace(hour=16), prices=(190, 320))

    BookingSystem(shows, venues).process()









