import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vehicles.settings")
django.setup()

from MyApp.models import Car

# List of remaining cars
remaining_cars = [
    {"car_name": "Kia", "car_desc": "Affordable and stylish.", "transmission": "Automatic",
     "deposit": 3500.00, "mileage": 22000, "age": 4, "image": "car/images/kia.jpg", "cost_per_day": 300.00},

    {"car_name": "Renault", "car_desc": "Practical and budget-friendly.", "transmission": "Manual",
     "deposit": 2800.00, "mileage": 27000, "age": 6, "image": "car/images/renault.jpg", "cost_per_day": 220.00},

    {"car_name": "Swift", "car_desc": "Compact and fuel-efficient.", "transmission": "Manual",
     "deposit": 2500.00, "mileage": 30000, "age": 5, "image": "car/images/swift.jpg", "cost_per_day": 200.00},

    {"car_name": "Taversa", "car_desc": "Spacious and comfortable.", "transmission": "Automatic",
     "deposit": 4200.00, "mileage": 18000, "age": 3, "image": "car/images/taversa.jpg", "cost_per_day": 350.00},

    {"car_name": "Innova", "car_desc": "Perfect for long drives and family trips.", "transmission": "Automatic",
     "deposit": 4800.00, "mileage": 16000, "age": 2, "image": "car/images/innova.jpg", "cost_per_day": 450.00},
]

# Add cars to the database
for car in remaining_cars:
    Car.objects.create(**car)

print("Remaining cars have been successfully added to the database.")
