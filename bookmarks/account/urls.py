from django.urls import path, include
from . import views

# URL patterns for including Django's built-in auth URLs and custom views for dashboard, registration, and profile editing.
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
