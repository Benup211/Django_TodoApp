from django.contrib import admin
from .models import ToDoItem,EventItem
# Register your models here.
admin.site.register(ToDoItem)
admin.site.register(EventItem)
