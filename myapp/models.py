from django.db import models

# Create your models here.
class userModel(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=60)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=40)
    email=models.EmailField()
    message=models.TextField(default="U r welcome")