from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=100, default="")
    car_desc = models.TextField(default="", blank=True)
    transmission = models.CharField(max_length=20, default="Manual")  # Manual/Automatic
    deposit = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)  # km ya da mil
    age = models.IntegerField(default=0)      # araç yaşı/model yılı
    cost_per_day = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images", default="")

    def __str__(self):
        return f"{self.car_name} - {self.transmission}"

class Office(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="")
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
            return f"{self.name} - {self.city}"
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")

    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    days_for_rent = models.IntegerField(default=0)
    date = models.DateField(null=True, blank=True)
    loc_from = models.CharField(max_length=50, default="")
    loc_to = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"Order #{self.order_id} - {self.name}"

class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150, default="")
    phone_number = models.CharField(max_length=15, default="")
    message = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
