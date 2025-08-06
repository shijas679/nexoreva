from django import forms

class StaffCodeForm(forms.Form):
    staff_code = forms.CharField(label="Enter Staff Code", max_length=20)

class LeaveRequestForm(forms.Form):
    staff_code = forms.CharField(label="Enter Staff Code", max_length=20)
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    reason = forms.CharField(widget=forms.Textarea)
