from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Dict, List


class EventType(Enum):
    ON_CLICK = auto()
    ON_SUBMIT = auto()


class Event:
    def __init__(self, payload: dict, event_type: EventType):
        self.payload = payload
        self.type = event_type


class Observer(ABC):
    @abstractmethod
    def update(self, event: Event):
        pass


class Publisher:
    def __init__(self):
        self.subscribers: Dict[EventType, List[Observer]] = {}

    def subscribe(self, event_type: EventType, callback: Observer):
        self.subscribers.setdefault(event_type, [])
        self.subscribers[event_type].append(callback)

    def unsubscribe(self, event_type: EventType, callback: Observer):
        self.subscribers[event_type] = [cb for cb in self.subscribers.get(event_type, []) if cb != callback]

    def notify(self, event: Event):
        for cb in self.subscribers.get(event.type, []):
            cb.update(event)

    def call_event(self, event: Event):
        print(f'Producer {event.type} called!')
        self.notify(event)


class EmailObserver(Observer):
    def update(self, event: Event):
        print(f'Sending email for event: {event.payload}!')


class OTPObserver(Observer):
    def update(self, event: Event):
        print(f'Sending OTP for event: {event.payload}!')


if __name__ == '__main__':
    p = Publisher()

    email_obs = EmailObserver()
    otp_obs = OTPObserver()

    p.subscribe(EventType.ON_CLICK, email_obs)

    p.subscribe(EventType.ON_SUBMIT, email_obs)
    p.subscribe(EventType.ON_SUBMIT, otp_obs)

    p.call_event(Event(payload=dict(message='clicked twice!'), event_type=EventType.ON_CLICK))

    p.call_event(Event(payload=dict(message='submitted once!'), event_type=EventType.ON_SUBMIT))
    print()

    p.unsubscribe(EventType.ON_SUBMIT, email_obs)
    p.call_event(Event(payload=dict(message='submitted twice!'), event_type=EventType.ON_SUBMIT))

