
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_job_listing, name='create_job_listing'),
    path('save/', views.save_textarea, name='save_textarea'),
    path('listings/', views.job_listings, name='listings'),
]
