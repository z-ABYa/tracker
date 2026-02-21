from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    application_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )
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