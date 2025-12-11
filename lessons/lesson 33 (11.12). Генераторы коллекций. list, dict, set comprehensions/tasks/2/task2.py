orders = [
    {"id": 110, "items": 2, "status": "pending"},
    {"id": 111, "items": 6, "status": "pending"},
    {"id": 112, "items": 4, "status": "done"},
    {"id": 113, "items": 1, "status": "pending"}
]
pending_orders = [
    f'Заказ #[{order["id"]}]: [{order["items"]}] позиций'
    for order in orders
    if order["status"] == 'pending' and 1 <= order['items'] <= 5
]

print(pending_orders)
