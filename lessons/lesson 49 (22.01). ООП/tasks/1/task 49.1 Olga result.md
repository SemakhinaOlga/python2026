Время затраченное на выполнение: 0:22

result: 10/100

1) **Сильные стороны**
- Студент начал правильно: импортировал `abc.ABC` и `abstractmethod`.
- Попытка создать абстрактный класс `NotificationChannel` с правильным названием.
- В абстрактном классе объявлен абстрактный метод `send`, что соответствует требованию.

2) **Ошибки и недочёты**

**Блокирующие (ломает выполнение требований задания)**
- Код неполный и содержит синтаксические ошибки. Файл не запустится.
  - В `NotificationChannel`: метод `format_message` не принимает `self`, но пытается использовать `sender_name` как переменную (строка 8). `sender_name` должен быть атрибутом экземпляра, а не класса, и передаваться в `__init__`. Это приведёт к `NameError`.
  - Классы `EmailChannel` и `SMSChannel` не завершены: после `def __init__(self, sender_name, sender_email):` и `def __init__(self, sender_name, sender_phone):` нет тела метода (только `pass` ожидается), что вызывает `IndentationError`.
  - Метод `send` в `EmailChannel` и `SMSChannel` не принимает обязательные аргументы `recipient` и `message` (требуется `def send(self, recipient: str, message: str):`). В текущем виде вызовет `TypeError`.
  - В `EmailChannel.send` и `SMSChannel.send` используется `super().format_message(message)`, но результат не сохраняется и не используется для печати. Кроме того, `message` не определена в области видимости метода.
  - Класс `NotificationService` не реализован вообще (есть только начало `class` без имени и тела).
  - Демонстрация работы (создание каналов, сервиса, вызов `notify_all`) отсутствует.
  - Требование "Нельзя создавать экземпляр `NotificationChannel` напрямую" формально соблюдено, но из-за ошибок в наследниках система неработоспособна.

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- В абстрактном классе `NotificationChannel` атрибут `sender_name` определён как атрибут класса со значением `"MyService"`. По условию, `sender_name` должен храниться в экземпляре (передаваться в `__init__`), чтобы каждый канал мог иметь своё имя. Сейчас все каналы будут использовать одно имя `"MyService"`, что противоречит идее инициализации с разными именами.
- Метод `format_message` в `NotificationChannel` не принимает `self`, поэтому не может получить `self.sender_name`. Это делает метод нефункциональным.

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- В абстрактном методе `send` в `NotificationChannel` можно добавить аннотации типов для ясности (`recipient: str, message: str` -> `None`), хотя это не строго требуется.
- Имена классов соответствуют условию, что хорошо.

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 5/50. Код нерабочий (синтаксические ошибки, нереализованные методы, отсутствие ключевых частей). Есть только каркас абстрактного класса.
- Качество кода (структура, читаемость, устойчивость, отсутствие дублирования): 3/30. Структура нарушена, код нечитаем из-за незавершённых конструкций, дублирование не оценивается из-за неполноты.
- Стиль и тесты: 2/20. Стиль не оценивается из-за критических ошибок. Тесты не требовались и не предоставлены.

Итог: 10/100 (округление от 5+3+2=10).

4) **Если задание выполнено не полностью**
- Отсутствует:
  - Корректная реализация `NotificationChannel` с `__init__`, принимающим `sender_name`, и методом `format_message`, использующим `self.sender_name`.
  - Реализация `EmailChannel.__init__` (сохранение `sender_name` и `sender_email`) и `EmailChannel.send` (печать в требуемом формате).
  - Реализация `SMSChannel.__init__` (сохранение `sender_name` и `sender_phone`) и `SMSChannel.send` (печать в требуемом формате).
  - Класс `NotificationService` с методом `notify_all`.
  - Демонстрация работы (создание объектов и вызовы).
- Сделано частично: объявлены классы с правильными именами, но без рабочей логики.

**Вариант полного решения (код):**

```python
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def __init__(self, sender_name: str):
        self.sender_name = sender_name

    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass

    def format_message(self, message: str) -> str:
        return f"[{self.sender_name}] {message}"

class EmailChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_email: str):
        super().__init__(sender_name)
        self.sender_email = sender_email

    def send(self, recipient: str, message: str) -> None:
        formatted = super().format_message(message)
        print(f"EMAIL to {recipient}: {formatted} (from {self.sender_email})")

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_phone: str):
        super().__init__(sender_name)
        self.sender_phone = sender_phone

    def send(self, recipient: str, message: str) -> None:
        formatted = super().format_message(message)
        print(f"SMS to {recipient}: {formatted} (from {self.sender_phone})")

class NotificationService:
    def __init__(self, channels: list[NotificationChannel]):
        self.channels = channels

    def notify_all(self, recipient: str, message: str) -> None:
        for channel in self.channels:
            channel.send(recipient, message)

# Демонстрация работы
if __name__ == "__main__":
    email = EmailChannel("MyService", "noreply@example.com")
    sms = SMSChannel("MyService", "+1234567890")
    service = NotificationService([email, sms])
    service.notify_all("user@example.com", "Hello via email and SMS!")
    service.notify_all("+0987654321", "Another notification.")
```
