from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Guest(models.Model):
    
    GuestID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    CNIC = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    ConfirmPassword = models.CharField(max_length=100)
    ContactNo = models.CharField(max_length=100)

class RoomType(models.Model):
    room_type = models.CharField(primary_key=True, max_length=100)
    room_desc = models.CharField(max_length=100)
    roomtype_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Adding room price field
    room_image = models.CharField(max_length=200)


class Room(models.Model):
    ROOM_STATUS_CHOICES = (
        ('available', 'Available'),
        ('booked', 'Booked'),
    )
    room_number = models.CharField(primary_key=True, max_length=10)
    occupancy = models.CharField(max_length=10)
    room_status = models.CharField(max_length=10, choices=ROOM_STATUS_CHOICES, default='available')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Room {self.room_number} - {self.room_status}"




class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    service_image = models.CharField(max_length=200)
    service_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.service_name


class BookedService(models.Model):
    booked_service_id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Booked service {self.service_name} for {self.guest}"
    

class Booking(models.Model):
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    services = models.ManyToManyField('Service')  # Include services booked
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)

    
    def calculate_total(self):
        room_price_per_night = self.room.room_type.roomtype_price
        check_in = self.check_in_date
        check_out = self.check_out_date
        # Calculate duration of stay in nights
        duration = (check_out - check_in).days
        # Calculate total room price based on duration
        total_room_price = room_price_per_night * duration
        services_price = sum(service.service_price for service in self.services.all())
        total_amount = total_room_price + services_price

        return total_amount





    
class Billing(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)



    
    
    
class Feedback(models.Model):
    FeedbackID = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Message = models.CharField(max_length=100)

    
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"