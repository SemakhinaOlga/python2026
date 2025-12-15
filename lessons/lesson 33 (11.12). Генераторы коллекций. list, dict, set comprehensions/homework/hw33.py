#1 задача
requests = [
    {"region": "msk", "priority": "urgent", "service": "backup"},
    {"region": "spb", "priority": "medium", "service": "backup"},
    {"region": "ekb", "priority": "high", "service": "sync"}
]
allowed_services = {"backup", "sync"}
target_regions = {
    req["region"].upper()
    for req in requests
    if req["priority"] in {"high", "urgent"} and req["service"] in allowed_services
}
print(target_regions)


#2 задача
result = [
    f"Эскалация #{ticket['id']} (уровень {ticket['level']}) — {ticket['owner'].strip()}"
    for ticket in tickets
    if ticket["status"] == "open"
    and 2<= ticket["level"] <= 4
    and ticket["owner"].strip() != ""
]


#3 задача
cluster_summary = {}

#4 задача
#logs = ["backend:create:15", "frontend:update:5", ...]
slow_services={
    service
    for log in logs
    for service, action, Sduration in [log.split(":", 2)]

    if action in ("create", "sync") and (duration := int(Sduration)) >= 20
}

brief=[
    f"{service} -> {action} (+{duration})"
    for log in logs
    for service, action, Sduration in [log.split(":", 2)]
    if (duration := int(Sduration)) < 20

]