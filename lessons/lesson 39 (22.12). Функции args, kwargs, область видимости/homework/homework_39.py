
def summarize_orders(*orders, **kwargs):

    if not orders:
        raise ValueError('Нет заказов для обработки')

    currency=kwargs.get('currency',"RUB")
    round_to=kwargs.get('round_to',2)# — сколько знаков оставить у среднего значения

    total_items=0
    for count in orders:
        name, number = count
        total_items+=number

#7
    avg_items=round(total_items/len(orders), round_to)
    return {
        "orders": len(orders),
        "total_items": total_items,
        "avg_items": avg_items,
        "currency": currency
    }








print(summarize_orders(("кофе", 2), ("чай", 1)))
# {'orders': 2, 'total_items': 3, 'avg_items': 1.5, 'currency': 'RUB'})
print(summarize_orders(("пицца", 3), ("салат", 1), round_to=1, currency="USD"))
# {'orders': 2, 'total_items': 4, 'avg_items': 2.0, 'currency': 'USD'})
#print(summarize_orders())
# ValueError: Нет заказов для обработки)
