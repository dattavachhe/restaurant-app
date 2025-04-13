

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='menu_images/',null=True,blank=True)

    def _str_(self):
        return self.name

class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField()
    guests = models.IntegerField()

    def _str_(self):
        return f"Reservation for {self.name}on{self.date}"