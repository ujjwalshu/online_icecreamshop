from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),  # Added trailing slash for consistency
    path("services/", views.services, name='services'),  # Changed to lowercase for consistency
    path("contact/", views.contact, name='contact'),  # Changed to lowercase for consistency
]
