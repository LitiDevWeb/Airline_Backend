from django.contrib import admin
from .models import Flight, Airport, Passenger

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination','duration')

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
# It's going to  tell django's admin app that 
# i would like to use the admin app to be able to manipule flights,Airports DB
