#1 задача

def format_product(name, price = 0):
    return f"Товар: {name}, Цена: {price} руб."
print(format_product("Молоко", 90))
print(format_product(price = 150, name = "Хлеб"))
print(format_product("Яблоки"))

#2 задача


def add_note(note, notes_list=None):
    if notes_list is None:
        notes_list = []
    notes_list.append(note)
    return notes_list

print(add_note("Купить молоко"))
print(add_note("Позвонить маме"))
my_list = []
print(add_note("Первая", my_list))
print(add_note("Вторая", my_list))

#3
def calculate_total(*args):
    if len(args) == 0:
        return 0
    return sum(args)
prices = [10, 20, 30]
print(calculate_total(*prices)) #60
print(calculate_total(100, 200, 50))
print(calculate_total(25))
print(calculate_total())

#4
cookbook = [
    {"name": "Омлет", "time": 10, "difficulty": "легко", "type": "завтрак"},
    {"name": "Борщ", "time": 120, "difficulty": "средне", "type": "обед"},
    {"name": "Салат", "time": 20, "difficulty": "легко", "type": "закуска"}
]

def find_recipes(**kwargs):
    result = []
    for recipe in cookbook:
        is_match = True
        for key, value in kwargs:
            if key == 'max_time':
                for recipe in cookbook:
                    if recipe["time"] > value:
                        is_match = False
                        break
            






print(find_recipes(difficulty="легко"))
print(find_recipes(max_time=30, dish_type="обед"))
print(find_recipes(name="Омлет"))