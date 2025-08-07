from django.db import models
import uuid

class WorkAssignment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    task_code = models.CharField(max_length=20, unique=True, editable=False)
    task_title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    assigned_to = models.ForeignKey('staff.Staff', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # <-- ADD THIS

    def save(self, *args, **kwargs):
        if not self.task_code:
            self.task_code = f"TASK-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.task_title
