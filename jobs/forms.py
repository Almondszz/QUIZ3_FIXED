from django import forms
from .models import JobApplicant, Job

class JobApplicantForm(forms.ModelForm):
    class Meta:
        model = JobApplicant
        fields = ['resume']

class JobForm(forms.ModelForm):
     class Meta:
        model = Job
        fields = ['job_title', 'job_description', 'location', 'min_offer', 'max_offer','image']
