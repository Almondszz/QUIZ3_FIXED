from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplicant
from .forms import JobApplicantForm, JobForm

@login_required
def job_apply(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if JobApplicant.objects.filter(user=request.user, job=job).exists():
        return render(request, 'jobs/already_applied.html', {'job': job})
    if request.method == 'POST':
        form = JobApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.user = request.user
            applicant.job = job
            applicant.save()
            return render(request, 'jobs/applied_success.html', {'job': job})
    else:
        form = JobApplicantForm()
    return render(request, 'jobs/job_apply.html', {'form': form, 'job': job})

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'create_job.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/jobs_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

class JobUpdateView(UpdateView):
    model = Job
    fields = ['job_title', 'job_description', 'min_offer', 'max_offer', 'location']
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/jobs_confirm_delete.html'
    success_url = reverse_lazy('job_list')