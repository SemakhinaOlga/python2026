from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    sender_name = "MyService"
    @abstractmethod
    def send(recipient: str, message: str):
        pass
    def format_message(message: str):
        return f"[{sender_name}] {message}"

class EmailChannel(NotificationChannel):
    def __init__(self, sender_name, sender_email):
    def send(self):
        super().format_message(message)
        print('')

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name, sender_phone):
    def send(self):
        super().format_message(message)

class
