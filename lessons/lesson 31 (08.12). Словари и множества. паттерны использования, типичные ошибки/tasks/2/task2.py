bookings = [('designers', 8), ('marketing', 5), ('designers', 4), ('startups', 6)]
finished = ['marketing']
hours=dict(bookings)

def summ(login, cost):
    orders[login] = hours.get(login, 0) + cost


fin_dict=dict.fromkeys(finished)


for i in hours:
    removed=fin_dict.pop(i,0)


print(hours)
