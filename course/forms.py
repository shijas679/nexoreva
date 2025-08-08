from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'sub_column', 'unicode', 'description', 'start_date', 'end_date', 'fees']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'id': 'id_name'}),
            'sub_column': forms.Select(attrs={'class': 'form-control', 'id': 'id_sub_column'}),
            'unicode': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_unicode', 'readonly': 'readonly', 'placeholder': 'Auto-generated'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fees': forms.NumberInput(attrs={'class': 'form-control'}),
        }