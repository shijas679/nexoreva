from django import forms
from staff.models import Staff
from workassignment.models import WorkAssignment

class TaskStatusUpdateForm(forms.Form):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    staff_code = forms.CharField(
        max_length=100,
        label='Staff Code',
        widget=forms.TextInput(attrs={'placeholder': 'Enter staff code', 'readonly': 'readonly'})
    )

    task_code = forms.CharField(
        max_length=100,
        label='Task Code',
        widget=forms.TextInput(attrs={'placeholder': 'Enter task code'})
    )
    
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        label='Status',
        widget=forms.Select()
    )
    
    def clean(self):
        cleaned_data = super().clean()
        staff_code = cleaned_data.get('staff_code')
        task_code = cleaned_data.get('task_code')
        
        if staff_code and task_code:
            # Check if staff exists
            try:
                staff = Staff.objects.get(staff_code=staff_code)
            except Staff.DoesNotExist:
                raise forms.ValidationError("Staff with this code does not exist.")
            
            # Check if task exists and is assigned to this staff
            try:
                task = WorkAssignment.objects.get(task_code=task_code, assigned_to=staff)
            except WorkAssignment.DoesNotExist:
                raise forms.ValidationError("Task not found or not assigned to this staff member.")
        
        return cleaned_data    