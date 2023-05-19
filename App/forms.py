from django import forms


class JobListingForm(forms.Form):
    job_position = forms.CharField(label='Job Position', max_length=100)
    tech_stack = forms.CharField(label='Tech Stack', max_length=500)
    company_name = forms.CharField(label='Company Name', max_length=100)
    company_values = forms.CharField(label='Company Values', max_length=500)
