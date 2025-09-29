from django.contrib import admin

# Register your models here.
from .models import userModel
class UserAdmin(admin.ModelAdmin):
    list_display=["name","city","state","email","phone"]

admin.site.register(userModel, UserAdmin)

# do this and do python3 manage.py makemigrations 
