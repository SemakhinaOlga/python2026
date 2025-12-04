list_books=[]
winter_books = ["Атлант", "Три товарища", "Скандинавские боги"]

friends_choice = ["Дом в котором", "Унесенные ветром"]
list_books.extend(winter_books)
list_books.extend(friends_choice)

print('Всего книг: ', len(list_books), '\nПервая книга: ', list_books[0],'\nПредпоследняя книга: ', list_books[-2])
for index, item in enumerate(list_books, start=1):
    print(f"{index}. {item}")
