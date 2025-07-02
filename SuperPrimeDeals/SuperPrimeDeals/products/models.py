from django.db import models
from django.utils import timezone

class Status(models.TextChoices):
    YES = '1', "YES"
    NO = '0', 'NO'

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    whatsInclude = models.TextField(null=True)
    imageInclude = models.ImageField(upload_to='images/')
    forWhom = models.TextField(null=True)

    status = models.CharField(max_length=1,choices= Status.choices, default=Status.YES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    comment = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.reviewer_name}"