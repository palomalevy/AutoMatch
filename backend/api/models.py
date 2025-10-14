from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class CarBrand(models.TextChoices):
    TOYOTA = "TOYOTA", "Toyota"
    HONDA = "HONDA", "Honda"
    FORD = "FORD", "Ford"
    BMW = "BMW", "BMW"
    MERCEDES = "MERCEDES", "Mercedes-Benz"
    AUDI = "AUDI", "Audi"
    TESLA = "TESLA", "Tesla"
    PORSCHE = "PORSCHE", "Porsche"
    HYUNDAI = "HYUNDAI", "Hyundai"
    KIA = "KIA", "Kia"
    NISSAN = "NISSAN", "Nissan"

def max_three(value):
    if value and len(value) > 3:
        raise ValidationError("You can select up to 3 favorite car brands.")

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=60, unique=True)
    passwordHash = models.CharField(max_length=255)
    zipCode = models.IntegerField()
    latitude = models.CharField(max_length=40, null=True, blank=True)
    longitude = models.CharField(max_length=40, null=True, blank=True)
    imageURL = models.URLField(null=True, blank=True)
    favorites = models.JSONField(default=list, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    externalId = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    region = models.CharField(max_length=120, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    latitude = models.CharField(max_length=40, null=True, blank=True)
    longitude = models.CharField(max_length=40, null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    imageURL = models.URLField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title