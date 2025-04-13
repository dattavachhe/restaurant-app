from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MenuItem, Reservation

admin.site.register(MenuItem)
admin.site.register(Reservation)