from django.db import models
from staff.models import Staff  # adjust if your Staff model is in a different app

class WorkAssignment(models.Model):
    assigned_to = models.ForeignKey(Staff, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    attachment = models.FileField(upload_to='assignments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_title} for {self.assigned_to.full_name}"
