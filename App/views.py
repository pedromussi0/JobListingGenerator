
from django.shortcuts import render
from .forms import JobListingForm
from .langchain_integration import *
from .models import JobListing


def create_job_listing(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            job_position = form.cleaned_data['job_position']
            tech_stack = form.cleaned_data['tech_stack']
            company_name = form.cleaned_data['company_name']
            company_values = form.cleaned_data['company_values']

            # Pass user input as input variables to generate_job_listing function
            job_listing = generate_job_listing(
                job_position=job_position,
                tech_stack=tech_stack,
                company_name=company_name,
                company_values=company_values
            )

            return render(request, 'App/create.html', {'job_listing': job_listing})
    else:
        form = JobListingForm()

    return render(request, 'App/create.html', {'form': form})


def save_textarea(request):
    if request.method == 'POST':
        content = request.POST.get('textarea_content')
        instance = JobListing(job_listing=content)
        instance.save()

        # summarizing job listing and assigning it to description
        summary = summarize_job_listing(job_listing=content)
        instance.description = summary
        instance.save()

    return render(request, 'App/create.html')
