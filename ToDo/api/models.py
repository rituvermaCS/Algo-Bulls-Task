from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.


class Task(models.Model):
    STATUS_CHOICE = (('OPEN', 'OPEN'), ('WORKING', 'WORKING'),
                     ('DONE', 'DONE'), ('OVERDUE', 'OVERDUE'))
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, null=False)
    due_data = models.DateField(null=True)
    tag = TaggableManager()
    status = models.CharField(max_length=7, choices=STATUS_CHOICE, null=False)
    objects = models.Manager()
