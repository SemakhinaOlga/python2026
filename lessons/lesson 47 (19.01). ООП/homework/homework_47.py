class Book:
    def __init__(self, title, author, pages):
        self.title=title
        self.author=author
        self.pages=pages

    def open(self):
        print(f'Книга "{self.title}" открыта на первой странице.')

    def read(self):
        print(f'Читаем книгу "{self.title}" автора {self.author}.')

    def close(self):
        print(f'Книга "{self.title}" закрыта.')

    def info(self):
        print(f'"{self.title}" - {self.author}, {self.pages} стр.')
book_1 = Book("1984", "Джордж Оруэлл", 328)
book_1.info()
book_1.open()
book_1.read()
book_1.close()


#2
class BankAccount:
    interest_rate = 0.05
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount < 0:
            print('Некореткная сумма')
        else:
            self.balance += amount
    def withdraw(self, amount):
        if amount < 0:
            print('Некореткная сумма')
        elif self.balance < amount:
            print("Недостаточно средств")
        else:
            self.balance-=amount
    def is_valid_amount(amount):
        if amount > 0:
            return True

    def set_interest_rate(self,new_rate):
        self.interest_rate=new_rate
        print('Процентная ставка изменена на {interest_rate}')

schet1 = BankAccount('человек 1', 200)
schet2 = BankAccount('человек 2', 400)
schet1.deposit(300)
schet2.withdraw(100)
schet1.set_interest_rate(0.2)


#3
class LibraryBook(Book):
    def __init__(self, title, author, pages, reader = None):
        self.reader = reader
        super().__init__(title, author, pages)

    def take(self, name):
        if self.reader is not None:
            print('Книга уже выдана')
        else:
            self.reader = name
            print(f'Книга выдана: {name}')
    def return_back(self):
        if self.reader is None:
            print('Книга и так в библиотеке')
        else:
            self.reader = None
            print('Книга возвращена')
Library_Book=LibraryBook("1984",'Джордж Оруэлл', 328)
Library_Book.take('Человек 1')
Library_Book.take('Человек 2')
Library_Book.return_back()
