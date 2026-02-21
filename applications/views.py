from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ApplicationForm

def home(request):
    return render(request, 'home.html')

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
