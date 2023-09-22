from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),    
    # main navigation
    path("clinic/", views.clinic, name="clinic"),
    path("dentists/", views.dentists, name="dentists"),
    path("team/", views.team, name="team"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("services/", views.services, name="services"),
    path("service_details/", views.service_details, name="service_details"),
    path("gallery/", views.gallery, name="gallery"),
    path("blog/", views.blog, name="blog"),
    path("allblogs/", views.allblogs, name="allblogs"),
    path("blog_n/", views.blog_n, name="blog_n"),
    path("blog_d/", views.blog_d, name="blog_d"),
    path("blog_e/<str:slug>", views.blog_e, name="blog_e"),
    path("blog_category/", views.blog_category, name="blog_category"),
    path("blog_category_n/", views.blog_category_n, name="blog_category_n"),
    path("blog_category_d/", views.blog_category_d, name="blog_category_d"),
    path("blog_category_e/", views.blog_category_e, name="blog_category_e"),
    path("blog_details/<int:blogid>", views.blog_details, name="blog_details"),
    
    path("contact_us/", views.contact_us, name="contact_us"),

    
    # functions
    path("appointment/", views.appointment, name="appointment"),
    path("directions/", views.directions, name="directions"),
    
    
    # admin
    path("adminpanel/", views.adminpanel, name="adminpanel"),
    ]
