from django import forms


class StaffCodeForm(forms.Form):
    staff_code = forms.CharField(label="Enter Staff Code", max_length=20)


class LeaveRequestForm(forms.Form):
    staff_code = forms.CharField(label="Enter Staff Code", max_length=20)
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    reason = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            classes = f'input-field {existing_classes}'.strip()
            field.widget.attrs.update({
                'placeholder': ' ',
                'class': classes,
            })
