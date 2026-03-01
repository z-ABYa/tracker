from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from .models import Application


@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user).order_by('-created_at')
    if status_filter := request.GET.get('status'):
        applications = applications.filter(status=status_filter)
        
    if query := request.GET.get('q'):
        applications = applications.filter(
            Q(company_name__icontains=query) |
            Q(role__icontains=query)
        )
    
    paginator = Paginator(applications, 5)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    
    statuses = Application.APPLICATION_STATUS
    return render(request, 'applications/dashboard.html', {
            'page_obj': page_obj,
            'current_status': status_filter,
            'statuses': statuses,
        })

@login_required
def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('dashboard')
    else:    
        form = ApplicationForm()
    return render(request, 'applications/create_application.html', {'form': form})

@login_required
def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    if request.method == 'POST':
        application.delete()
        return redirect('dashboard')
    
    return render(request, 'applications/confirm_delete.html', {'application': application})

@login_required
def edit_application(request, pk):
    application = get_object_or_404(Application, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
            
    form = ApplicationForm(instance=application)
    return render(request, 'applications/edit_application.html', {'form': form})
