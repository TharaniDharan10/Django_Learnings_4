from django.contrib import admin

# Register your models here.
from .models import userModel
class UserAdmin(admin.ModelAdmin):
    list_display=["name","phone","city","state","email","message"]

admin.site.register(userModel, UserAdmin)

# do this and do python3 manage.py makemigrations 
