from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application


@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'applications/dashboard.html', {'applications': applications})

@login_required
def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('/')
    else:    
        form = ApplicationForm()
    return render(request, 'applications/create_application.html', {'form': form})
