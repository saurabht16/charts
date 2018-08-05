from django.contrib import admin
from .models import Passenger, emp
# Register your models here.


class PassengerAdmin(admin.ModelAdmin):
    pass

class empAdmin(admin.ModelAdmin):
    pass

admin.site.register(Passenger,PassengerAdmin)
admin.site.register(emp,empAdmin)
