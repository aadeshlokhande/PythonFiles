from django.db import models
from datetime import datetime

class IsDelete(models.TextChoices):
    yes = '1', 'YES'
    no = '0', 'NO'

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    mobile = models.CharField(max_length=12,null=False)
    password = models.CharField(max_length=255,null=False)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateField()
    is_delete = models.CharField(max_length=1,choices=IsDelete, default=IsDelete.no)
