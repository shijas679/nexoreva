from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'sub_column', 'description', 'start_date', 'end_date', 'fees']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'id': 'id_name'}),
            'sub_column': forms.Select(attrs={'class': 'form-control', 'id': 'id_sub_column'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fees': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Empty by default; JS will populate based on course selection
        self.fields['sub_column'].choices = [('', '---------')]
