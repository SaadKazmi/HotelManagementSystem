from django.contrib import admin
from .models import *  # Import your Guest model here
#from .models import Room
# Register your models here.
#admin.site.register(Room)


class GuestInfo(admin.ModelAdmin):
    list_display=('GuestID','FirstName', 'LastName','Email','CNIC')

class RoomTypeInfo(admin.ModelAdmin):
    list_display=('room_type','room_desc', 'roomtype_price')
    
class RoomInfo(admin.ModelAdmin):
    list_display=('room_number','occupancy', 'room_status','room_type')
    
class ServiceInfo(admin.ModelAdmin):
    list_display=('service_id','service_name', 'service_price')
    
class BookingInfo(admin.ModelAdmin):
    list_display=('guest','room', 'check_in_date','check_out_date',)
    
class BillingInfo(admin.ModelAdmin):
    list_display=('booking','total_amount')

class StaffInfo(admin.ModelAdmin):
    list_display=('first_name','last_name', 'role','contact_no',)

admin.site.register(Guest, GuestInfo)  
admin.site.register(RoomType, RoomTypeInfo) 
admin.site.register(Room, RoomInfo)
admin.site.register(Service, ServiceInfo)
admin.site.register(Booking, BookingInfo)
admin.site.register(Billing, BillingInfo)
admin.site.register(Staff, StaffInfo)

