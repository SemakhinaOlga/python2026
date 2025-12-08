shops = [
    ('Nevsky', '2025-12-04 06:30'),
    ('Kazan', '2025-12-05 08:15'),
    ('Fontanka', '2025-12-03 18:00'),
]
calibration=dict(shops)
urgent_location = 'Kazan'
new_location = 'Admiral'

print(urgent_location,'->', calibration.get(urgent_location, 'не калибрована'))
print(new_location,'->', calibration.get(new_location, 'не калибрована'))
    
