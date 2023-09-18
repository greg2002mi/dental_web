from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.paginator import Paginator
from django.core.paginator import (EmptyPage, PageNotAnInteger,
Paginator)
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Home, Global, Gallery, Reservation, Service, ServiceDetails, Team, Staff, Category, Contact_us, BlogPost, Comment, FAQCategory, FAQ, FAQComment
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
# from .forms import ()
import os, uuid, json, re
from uuid import uuid4
from django.db.models import Q
from datetime import datetime
from django.utils import timezone
from django.core.mail import send_mail  # later to send mail - send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView
from io import BytesIO


# Main Navigation.
def index(request):
    return render (request, "index.html", context={})

def clinic(request):
    return render (request, "clinic.html", context={})

def dentists(request):
    return render (request, "dentists.html", context={})

def team(request):
    return render (request, "team.html", context={})

def testimonials(request):
    return render (request, "testimonials.html", context={})

def services(request):
    services = Service.objects.all()
    context={
        'services': services,
        }
    return render (request, "services.html", context)

def service_details(request):
    return render (request, "service_details.html", context={})

def gallery(request):
    return render (request, "gallery.html", context={})

def blog(request):
    return render (request, "blog.html", context={})

def blog_details(request):
    return render (request, "blog_details.html", context={})

def contact_us(request):
    return render (request, "contact_us.html", context={})


# general functions 
def appointment(request):
    return render (request, "appointment.html", context={})

def directions(request):
    return render (request, "directions.html", context={})








