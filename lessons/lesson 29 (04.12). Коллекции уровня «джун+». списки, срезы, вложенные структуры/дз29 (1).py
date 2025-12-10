base_ingredients = ["мука", "сахар", "яйца"]
additional_ingredients = ["масло", "разрыхлитель"]
base_ingredients.extend(additional_ingredients)
for index, item in enumerate(base_ingredients, start=1):
    print(f"{index}. {item}")

cooking_times = [10, 15, 20, 25, 30, 35, 40, 45, 50]
print('Быстрые блюда:', cooking_times[:3])
print('Долгие блюда:', cooking_times[-3:])
print('Среднее время:', cooking_times[1:5])
print('Каждое третье блюдо:', cooking_times[::3])


steps = ["полить цветы", "вынести мусор", "помыть посуду", "протереть полки"]
new_steps=["протереть пыль","пропылесосить"]
steps.extend(new_steps)
steps.insert(2, 'помыть окна')
steps.remove('вынести мусор')

last_step=steps.pop(-1)
steps.insert(0,last_step)
print(steps)


recipes = [
    {"название": "Чизкейк", "тип": "десерт", "время_приготовления": 60},
    {"название": "Салат Цезарь", "тип": "закуска", "время_приготовления": 20},
    {"название": "Паста Карбонара", "тип": "основное", "время_приготовления": 30},
    {"название": "Тирамису", "тип": "десерт", "время_приготовления": 45}
]
for i in recipes:
    print(f"{i['название']}: {i['тип']} ({i['время_приготовления']})")
    
for i in recipes:
    if i['время_приготовления']<30:
        quick_recipes=[(f"{i['название']}")]

        

for i in recipes:
    if i['тип']=="дессерт":
        cakes=[(f"{i['название']}: {i['тип']}")]

time=0
for i in recipes:
    time+=i['время_приготовления']
    average=time/len(recipes)
print('среднее вермя приготовления:',average)

