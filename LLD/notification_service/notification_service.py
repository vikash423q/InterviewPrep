"""
Design a Notification Manager System

Notification channels : email/text/push
Different Topics :register, password change, order placed, marketing, Sales, news topics etc.
User preference : User can opt-out for particular topic (ex. marketing)
Send to single user or bulk users
Notification Queuing (Important)
Tracking status (Processing, Delivered, Clicked)
Scheduling Notifications: (if we have extra time)
"""
import threading
import time
import uuid
from collections import deque
from enum import Enum
from typing import List, Dict, Union, Deque
from abc import ABC, abstractmethod


class NotificationStatus(Enum):
    PROCESSING = 'processing'
    DELIVERED = 'delivered'
    CLICKED = 'clicked'

class NotificationChannelEnum(Enum):
    EMAIL = 'email'
    TEXT = 'text'
    PUSH = 'push'


class User:
    def __init__(self, name: str, email: str = "", phone: str = "", device_id: str = ""):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.device_id = device_id

    def __repr__(self):
        return self.name


class Topic:
    def __init__(self, name: str):
        self.name = name
        self.subscribers = set()

    def subscribe(self, user: User):
        self.subscribers.add(user.id)

    def un_subscribe(self, user: User):
        if user in self.subscribers:
            self.subscribers.remove(user.id)


class NotificationSender:
    def __init__(self, name):
        self.name = name

class Notification(ABC):
    def __init__(self, message: str, topic: Topic, sender: NotificationSender, channel: NotificationChannelEnum,
                 receiver: User = None):
        self.sender = sender
        self.channel: NotificationChannelEnum = channel
        self.message = message
        self.topic = topic
        self.receiver: Union[User, None] = receiver


class NotificationMessage:
    def __init__(self, user: User, notification: Notification):
        self.user = user
        self.notification = notification
        self.status: NotificationStatus = NotificationStatus.PROCESSING


class NotificationQueue:
    def __init__(self):
        self.queue: Deque[NotificationMessage] = deque()
        self.t = threading.Thread(target=self.process)

    def add_notification(self, notification: NotificationMessage):
        notification.status = NotificationStatus.PROCESSING
        self.queue.append(notification)

    def process(self):
        while True:
            if self.queue:
                notification = self.queue.popleft()
                print(f'Message: {notification.notification.message} sent to user: {notification.user} through {notification.notification.channel.name}')
                notification.status = NotificationStatus.DELIVERED
            time.sleep(1)

    def start(self):
        print('Notification Queue started')
        self.t.start()
        # self.t.join()


class NotificationChannel(ABC):
    def __init__(self, notification_queue: NotificationQueue):
        self.queue : NotificationQueue = notification_queue
        self.queue.start()

    @abstractmethod
    def send(self, message: NotificationMessage):
        pass

class EmailNotificationChannel(NotificationChannel):
    def send(self, message: NotificationMessage):
        self.queue.add_notification(message)

class SMSNotificationChannel(NotificationChannel):
    def send(self, message: NotificationMessage):
        self.queue.add_notification(message)

class PushNotificationChannel(NotificationChannel):
    def send(self, message: NotificationMessage):
        self.queue.add_notification(message)


class NotificationChannelStrategy:
    _channels = {
        NotificationChannelEnum.EMAIL: EmailNotificationChannel(NotificationQueue()),
        NotificationChannelEnum.TEXT: SMSNotificationChannel(NotificationQueue()),
        NotificationChannelEnum.PUSH: PushNotificationChannel(NotificationQueue())
    }

    @staticmethod
    def get_channel(notification: Notification):
        if notification.channel in NotificationChannelStrategy._channels:
            return NotificationChannelStrategy._channels[notification.channel]


class TopicManager:
    def __init__(self):
        self.topics: Dict[str, Topic] = {}

    def add_topic(self, name: str):
        self.topics[name] = Topic(name)

    def get_topic(self, name: str) -> Union[Topic, None]:
        return self.topics.get(name)

    def add_subscriber(self, topic_name: str, user: User):
        topic = self.get_topic(topic_name)
        topic.subscribe(user)

    def remove_subscriber(self, topic_name: str, user: User):
        topic = self.get_topic(topic_name)
        topic.un_subscribe(user)


class UserManager:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, name: str, email: str = "", phone: str = "", device_id: str = ""):
        user = User(name, email, phone, device_id)
        self.users[user.id] = user
        return user

    def get_user(self, user_id: str) -> Union[User, None]:
        return self.users.get(user_id)


class NotificationManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NotificationManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.user_manager = UserManager()
        self.topic_manager = TopicManager()

    def add_topic(self, name: str):
        self.topic_manager.add_topic(name)
        return self.topic_manager.get_topic(name)

    def add_subscriber(self, topic_name: str, user: User):
        self.topic_manager.add_subscriber(topic_name, user)

    def remove_subscriber(self, topic_name: str, user: User):
        self.topic_manager.remove_subscriber(topic_name, user)

    def send_notification(self, notification: Notification):
        channel = NotificationChannelStrategy.get_channel(notification)

        if notification.receiver:
            channel.send(NotificationMessage(notification.receiver, notification))
            return

        for user_id in notification.topic.subscribers:
            channel.send(NotificationMessage(self.user_manager.get_user(user_id), notification))


if __name__ == '__main__':
    notification_manager = NotificationManager()

    # Adding topics
    sports_topic = notification_manager.add_topic('sports')
    games_topic = notification_manager.add_topic('games')
    politics_topic = notification_manager.add_topic('politics')

    # Adding user
    vikash = notification_manager.user_manager.add_user("Vikash")
    akash = notification_manager.user_manager.add_user("Akash")
    rohit = notification_manager.user_manager.add_user("Rohit")
    sudhanshu = notification_manager.user_manager.add_user("Sudhanshu")

    # Subscribing users
    notification_manager.add_subscriber("politics", vikash)
    notification_manager.add_subscriber("politics", akash)
    notification_manager.add_subscriber("politics", sudhanshu)

    notification_manager.add_subscriber("games", vikash)
    notification_manager.add_subscriber("games", rohit)

    notification_manager.add_subscriber("sports", rohit)

    # sending notifications
    sender = NotificationSender('Anonymous')

    notificaton = Notification("India has released it's new budget!", politics_topic, sender, NotificationChannelEnum.EMAIL)
    notification_manager.send_notification(notificaton)

    notificaton = Notification("Sony has reduced the PS5 prices", games_topic, sender, NotificationChannelEnum.PUSH)
    notification_manager.send_notification(notificaton)

    notificaton = Notification("New world record created by Ronaldo", sports_topic, sender,
                               NotificationChannelEnum.EMAIL, akash)
    notification_manager.send_notification(notificaton)


