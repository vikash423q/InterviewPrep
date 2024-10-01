# Building a logger system
# It should have the following features:
# It should support multiple handler
# It should support a formatter for each handler
# It should have different log levels

import os
import requests
from threading import Lock
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    CRITICAL = 4
    ERROR = 5


class Record:
    def __init__(self, message: str, level: LogLevel):
        self.level = level
        self.message = message
        self.created = datetime.now()

    def to_dict(self):
        return {
            "level": self.level.name,
            "message": self.message,
            "created": self.created
        }


class Formatter:
    def __init__(self, fmt: str):
        self.fmt = fmt

    def format(self, record: Record) -> str:
        return self.fmt.format(**record.to_dict())


class Handler:
    def __init__(self):
        self.formatter = Formatter("[{level}] {created} {message}")
        self.lock = Lock()

    def add_formatter(self, formatter: Formatter):
        self.formatter = formatter

    def emit(self, record):
        with self.lock:
            print(self.formatter.format(record))


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.handlers = [Handler()]
        self.level = LogLevel.DEBUG

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    def set_level(self, log_level: LogLevel):
        self.level = log_level

    def log_data(self, level: LogLevel, message: str):
        if level.value >= self.level.value:
            record = Record(message, level)
            for handler in self.handlers:
                try:
                    handler.emit(record)
                except Exception as e:
                    print('Error while emitting message:', str(e))

    def info(self, message: str):
        self.log_data(LogLevel.INFO, message)

    def debug(self, message: str):
        self.log_data(LogLevel.DEBUG, message)

    def warning(self, message: str):
        self.log_data(LogLevel.WARNING, message)

    def critical(self, message: str):
        self.log_data(LogLevel.CRITICAL, message)

    def error(self, message: str):
        self.log_data(LogLevel.ERROR, message)


class FileHandler(Handler):
        def __init__(self, filepath: str):
            super().__init__()
            self.filepath = filepath
            directory = os.path.dirname(self.filepath)
            if directory:
                os.makedirs(directory, exist_ok=True)


        def emit(self, record):
            with open(self.filepath, 'a') as f:
                f.write(self.formatter.format(record)+'\n')


if __name__ == '__main__':
    logger = Logger()
    logger.set_level(LogLevel.INFO)

    class WebhookHandler(Handler):
        def __init__(self, url):
            super().__init__()
            self.url = url

        def emit(self, record):
            requests.post(self.url, json={'message': self.formatter.format(record)})


    webhook_handler = WebhookHandler('https://webhook.site/cc8334f9-ff9f-42a1-b50e-e5b06ea6788d')
    webhook_handler.add_formatter(Formatter("SENT AT {created} {message}"))
    logger.add_handler(webhook_handler)
    logger.add_handler(FileHandler('test.log'))


    logger.debug('this is a debug log message')
    logger.info('this is a info log message')
    logger.warning('this is a warning log message')
    logger.critical('this is a critical log message')
    logger.error('this is a error log message')