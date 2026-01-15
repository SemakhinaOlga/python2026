def print_attendees(path: str):
    try:
        with open('../example.txt', 'r') as file:
            content=file.read()
            n=len(content)
            print(f'Участники{n}')
            for line in content.split():
                print(f'{line.strip()}\n')
    except FileNotFoundError:
        print('Нет файла со списком участников')
    except ValueError as e:
        print('Список участников пуст')
print(print_attendees('../example.txt'))
