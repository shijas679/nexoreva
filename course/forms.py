from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'sub_course', 'description', 'start_date', 'end_date', 'payment_amount']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'id': 'id_course_name'}),
            'sub_course': forms.Select(attrs={'class': 'form-control', 'id': 'id_sub_course'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter course description'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter payment amount'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_course'].choices = [('', '---------')]
