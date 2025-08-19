from django.contrib import admin
from .models import Booking


"""
Admin setup for Booking model: displays key fields, allows filtering by date/table, and supports search by name/user.
"""
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'table_number', 'date', 'time', 'user')
    list_filter = ('date', 'table_number')
    search_fields = ('name', 'user__username')
