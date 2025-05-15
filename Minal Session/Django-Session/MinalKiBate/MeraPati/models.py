from django.db import models
from django.utils import timezone

class Status(models.TextChoices):
    yes = "1", 'YES'
    no = '0', 'NO'

# Create your models here.
class MeraPati(models.Model):
    Tech_level = [
        ('0', 'fresher'),
        ('1', 'mediam'),
        ('2', 'experianced')
    ]

    Choice = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Choice)

    job = models.CharField(max_length=255)
    maritialStatus = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    spiritual = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    vegitarian = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    supportive = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    loyal = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    trustable = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    carring = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    mature = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    childish = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    fit = models.CharField(max_length=1,choices=Status.choices,default=Status.no)
    salary = models.IntegerField()
    tech_strong = models.CharField(max_length=1, choices=Tech_level)
    create_at = models.DateTimeField(default=timezone.now)


# job, unmarried, spiritual, vegitarian, supportive, loyal, trustable, carring, mature, childish, fit, salary > 150000, technical strong.

# enum ---> sql 
