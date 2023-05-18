from django.shortcuts import render, redirect
from .forms import JobListingForm
from .langchain_integration import *
from .models import JobListing


def create_job_listing(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            job_position = form.cleaned_data['job_position']
            request.session['job_position'] = job_position

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
        job_position = request.session.get('job_position')

        if content and job_position:
            instance = JobListing(
                job_title=job_position,
                description=summarize_job_listing(job_listing=content),
                job_listing=content
            )
            instance.save()

    return redirect(create_job_listing)


def job_listings(request):
    listings = JobListing.objects.all()
    return render(request, 'App/listings.html', {'listings': listings})
