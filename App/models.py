from django.db import models


class JobListing(models.Model):
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    job_listing = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title
