from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    
    # main navigation
    path("clinic/", views.clinic, name="clinic"),
    path("dentists/", views.dentists, name="dentists"),
    path("team/", views.team, name="team"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("services/", views.services, name="services"),
    path("service_details/", views.service_details, name="service_details"),
    path("gallery/", views.gallery, name="gallery"),
    path("blog/", views.blog, name="blog"),
    path("blog_details/", views.blog_details, name="blog_details"),
    path("contact_us/", views.contact_us, name="contact_us"),

    
    # functions
    path("appointment/", views.appointment, name="appointment"),
    path("directions/", views.directions, name="directions"),
    
    
    # admin
    
    ]
