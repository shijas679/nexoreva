from django.db import models
from staff.models import Staff
from workassignment.models import WorkAssignment

# Create your models here.

class task_status(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
    ]
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='task_status')
    task = models.ForeignKey(WorkAssignment, on_delete=models.CASCADE, related_name='task_status')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)