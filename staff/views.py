
from django.shortcuts import render, redirect
from .forms import StaffForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Staff member added successfully.")
            return redirect('add_staff')  
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = StaffForm()

    return render(request, 'staff/add_staff.html', {'form': form})

from django.shortcuts import render
from .models import Staff
from django.contrib.auth.decorators import login_required

@login_required
def view_staff(request):
    staff_list = Staff.objects.all().order_by('-id')  # Latest first
    return render(request, 'staff/view_staff.html', {'staff_list': staff_list})
