requests = [
    {"service": "auth", "priority": "high", "region": "msk"},
    {"service": "billing", "priority": "low", "region": "ekb"},
    {"service": "storage", "priority": "urgent", "region": "msk"}
]
allowed_services = {"auth", "storage"}


target_regions = [
    f'{req["region"]}'
    for req in requests
    if req["priority"] in {"high", "urgent"} and req["service"] in allowed_services
]

print(set(target_regions))
