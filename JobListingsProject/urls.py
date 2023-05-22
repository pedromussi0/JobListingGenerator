from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.CustomLoginView.as_view(template_name='App/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/register/', views.register_view, name='register'),
    path('', views.create_job_listing, name='create_job_listing'),
    path('save/', views.save_textarea, name='save_textarea'),
    path('listings/', views.job_listings, name='listings'),
]
