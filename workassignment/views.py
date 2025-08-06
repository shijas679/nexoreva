# views.py
from django.shortcuts import render, get_object_or_404, redirect
from staff.models import Staff
from .models import WorkAssignment
from .forms import WorkAssignmentForm

# Home: show list of staff (employees or interns)
def home(request):
    users = Staff.objects.filter(role__in=['Intern', 'Employee'], status='Active')
    return render(request, 'workassignment/user_list.html', {'users': users})

# Detail view: show staff and their tasks
def user_detail(request, user_id):
    user = get_object_or_404(Staff, id=user_id)
    assignments = WorkAssignment.objects.filter(assigned_to=user)
    return render(request, 'workassignment/user_detail.html', {
        'user': user,
        'assignments': assignments
    })

# Add new task to user
def add_assignment(request, user_id):
    user = get_object_or_404(Staff, id=user_id)
    if request.method == 'POST':
        form = WorkAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.assigned_to = user
            assignment.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = WorkAssignmentForm()
    return render(request, 'workassignment/add_assignment.html', {
        'form': form,
        'user': user
    })
