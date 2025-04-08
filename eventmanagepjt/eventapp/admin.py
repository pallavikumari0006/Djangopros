from django.contrib import admin
from.models import Event
from .models import Booking
# Register your models here.
admin.site.register(Event)
 

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','cus_name','cus_ph','name','booking_date','booking_on')#list of all names from model
admin.site.register(Booking,BookingAdmin)