from django.db import models
from django.utils import timezone

priorityChoices = [
    ('H','High'),
    ('M', 'Mediam'),
    ('L', 'Low')
]

statusChoices = [
    ('P', 'Pending'),
    ('C', 'Completed')
]


# Create your models here.
class ToDoModel(models.Model):
    title = models.CharField(max_length=50)
    priority = models.CharField(max_length=1,choices=priorityChoices,default='M')
    notes = models.TextField()
    status = models.CharField(max_length=1, choices=statusChoices, default='P')
    duedate = models.DateField(default=timezone.localtime(timezone.now()).date()) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
