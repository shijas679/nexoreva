from django import forms
from .models import WorkAssignment

class WorkAssignmentForm(forms.ModelForm):
    class Meta:
        model = WorkAssignment
        fields = ['task_title', 'description', 'start_date', 'end_date', 'attachment']
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
