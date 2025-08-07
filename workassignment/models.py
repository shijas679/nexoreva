from django.db import models
from staff.models import Staff

class WorkAssignment(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    task_title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    attachment = models.FileField(upload_to='assignments/', blank=True, null=True)
    assigned_to = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='assignments')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return f"{self.task_title} - {self.assigned_to}"
