#1 задача

bookings = [
    ("designers", 8),
    ("marketing", 5),
    ("designers", 4),
    ("startups", 6),
]
finished = ["marketing"]
hours={}
for team, time in bookings:
    hours[team]=hours.get(team,0)+time
for team in finished:
    remove=hours.pop(team, '0')
    print(f'Удалили: {team}, с часами: {remove}')
print('итог:', hours)

#2 задача
rooms = [
    ("blue", "09:00"),
    ("green", "10:30"),
    ("blue", "15:00"),
]
checked = ["blue", "red"]
last_booking={}
for room, time in rooms:
    last_booking[room]=time
for room in checked:
    print(f'{room} -> {last_booking.get(room, 'свободно')}')


#задача 3
emails = [
    "olga@shop.ru",
    "user1@corp.ru",
    "user2@corp.ru",
    "friend@gmail.com",
]
trusted = {"corp.ru"}

count_by_domain={}

all_domains = set()

for mail in emails:
    domain = mail.split('@')
    count_by_domain[domain] = count_by_domain.get(domain, 0) + 1
    all_domains.add(domain)
no_trusted = all_domains - trusted

print("count_by_domain =", count_by_domain)
print("all_domains =", all_domains)
print("not_trusted =", no_trusted)

#4 задача
items = [
    ("notebook", 3),
    ("pen", 10),
    ("marker", 2),
    ("notebook", 4),
]
limit = 5
stock={}
for item, count in items:
    stock[item]= stock.get(name,0) +count
stock_limit={}
for item, count in items:
    stock_limit[item]=
print('сток=', stock)
print('товары с остатком больше limit=', stock_limit)
