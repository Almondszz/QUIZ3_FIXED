from django.conf import settings
from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    location = models.CharField(max_length=255)
    min_offer = models.DecimalField(max_digits=10, decimal_places=2)
    max_offer = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)

    def __str__(self):
        return self.job_title

class JobApplicant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.user.username} applied for {self.job.job_title}"