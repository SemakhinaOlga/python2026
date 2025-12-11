projects = [
    {"title": "Docs", "members": ["Анна"], "status": "active"},
    {"title": "Parser", "members": ["Илья", "Рита", "Кирилл"], "status": "active"},
    {"title": "ETL", "members": ["Оля", "Марк", "Сева", "Катя", "Том"], "status": "paused"}
]
active_project={item['title']: len(item['members']) for item in projects if item['status'] == 'active' and 2 <= len(item['members']) <= 5}
print(active_project)
