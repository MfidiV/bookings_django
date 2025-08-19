from django.db import models
from django.contrib.auth.models import User



class Booking(models.Model):
    """
    Model representing a table booking made by a user.
	Table booking is linked to Django's built in user model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Booking associated with a user, deletebookinf if user removed
    name = models.CharField(max_length=100)
    table_number = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - Table {self.table_number}"
