from django.contrib.auth.models import User
from django.db import models


class Application(models.Model):
    APPLICATION_STATUS_APPLIED = 'A'
    APPLICATION_STATUS_INTERVIEW = 'I'
    APPLICATION_STATUS_REJECTED = 'R'
    APPLICATION_STATUS_OFFER = 'O'

    APPLICATION_STATUS = [
        (APPLICATION_STATUS_APPLIED , 'Applied'),
        (APPLICATION_STATUS_INTERVIEW , 'Interview'),
        (APPLICATION_STATUS_REJECTED , 'Rejected'),
        (APPLICATION_STATUS_OFFER , 'Offer')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    application_date = models.DateField()
    status = models.CharField(max_length=1, choices=APPLICATION_STATUS, default=APPLICATION_STATUS_APPLIED)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.role}"
    