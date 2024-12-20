from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    number = models.CharField(max_length=30)
    capacity = models.IntegerField()
    location = models.TextField()

    def __str__(self):
        return f"Room: {self.number}\nCapacity: {self.capacity}"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client:{self.user}\nRoom:{self.room}"
    
