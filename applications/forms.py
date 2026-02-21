from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'company_name',
            'role',
            'location',
            'application_date',
            'status',
            'notes'
        ]