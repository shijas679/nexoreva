from django.db import models
from staff.models import Staff  # Adjust import based on your project layout

class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.staff.full_name} - {self.date}"

class LeaveRequest(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')  # For future approval process
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.full_name} - {self.from_date} to {self.to_date}"
