spending = [1800, 2400, 3100, 950, 2700, 1200, 4000]
new_list=[(f'День {index}: {item}₽') for index, item in enumerate(spending, start = 1) if item>2000]
print(new_list)
