from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def dashboard_view(request):
    # Replace with actual logic later
    context = {
        'total_staff': 12,
        'total_departments': 4,
        'total_interns': 5,
    }
    return render(request, 'dashboard/dashboard.html', context)
