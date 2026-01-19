class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def open(self):
        print(f'Книга {self.title} открыта на первой странице.')
    def read(self):
        print(f'Читаем книгу {self.title} автора {self.author}.')
    def close(self):
        print(f'Книга {self.title} закрыта.')
    def info(self):
        print(f'"{self.title}" - {self.author}, {self.pages} стр.')

book_1 = Book('1984', 'Джордж Оруэлл',328)

book_1.info()
book_1.open()
book_1.read()
book_1.close()