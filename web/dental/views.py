from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.paginator import Paginator
from django.core.paginator import (EmptyPage, PageNotAnInteger,
Paginator)
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Home, Global, Gallery, Reservation, Service, ServiceCat, Team, Staff, Category, Contact_us, BlogPost, Comment, FAQCategory, FAQ, FAQComment
from .forms import NewBlogCatForm, EditBlogForm, BlogPostForm
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
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail  # later to send mail - send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView
from io import BytesIO
import itertools


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

''' CRUD Blog '''
def blog(request):
    current_date = timezone.now()
    six_months_ago = current_date - timedelta(days=180)
    # to show only either recent 30 
    if BlogPost.objects.filter(dateTime__gte=six_months_ago).exists():
        blog = BlogPost.objects.filter(dateTime__gte=six_months_ago).order_by('-dateTime')[:12]
    else:
        blog = BlogPost.objects.all().order_by('-dateTime')[:12]
    allblogs = BlogPost.objects.all().order_by('-dateTime')  
    grouped_blog = []
    listbythree = []
    delay_values = [200, 400, 600]
    delay_iterator = itertools.cycle(delay_values)
    total = len(blog)
    control = total
    for i, post in enumerate(blog):
        # Create a dictionary for each post with the required fields
        post_dict = {
            'id': post.id,
            'title': post.title,
            'short': post.short,
            'delay': next(delay_iterator)  # Get the next delay value from the iterator
        }
        
        listbythree.append(post_dict)
        
        if len(listbythree) == 3:
            grouped_blog.append(listbythree)
            control = control - 3
            listbythree = []
        if total == i + 1 & control < 3:
            grouped_blog.append(listbythree)
    context={
        'gr_blog': grouped_blog,
        'blogs': allblogs
        }
    return render (request, "blog.html", context)



@login_required
def allblogs(request):
    return render (request, "blog.html", context={})

@login_required
def blog_n(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid(): 
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, _("Your blog is on air."))
            return redirect('blog_details', blog.id)
    else:
        context={
            'form': BlogPostForm(),
            }
    return render (request, "blog_n.html", context)

@login_required
def blog_e(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = EditBlogForm(request.POST, instance=blog)
        if form.is_valid(): 
            form.save()
            messages.success(request, _("Your blog is on air."))
            return redirect('blog_details', blog.id)
    else:
        context={
            "blog": blog,
            'form': EditBlogForm(instance=blog),
            }
    return render (request, "blog_e.html", context)

@login_required
def blog_d(request, slug):
    return render (request, "blog.html", context={})

@login_required
def blog_category(request):
    blogcat = Category.objects.all()
    
    context={
        'blogcat': blogcat, 
        'new_bc': NewBlogCatForm()
        }
    return render (request, "blog_category.html", context)

@login_required
def blog_category_n(request):
    return render (request, "blog.html", context={})

@login_required
def blog_category_e(request):
    return render (request, "blog.html", context={})

@login_required
def blog_category_d(request):
    return render (request, "blog.html", context={})

def blog_details(request, blogid):
    blog = get_object_or_404(BlogPost, pk=blogid)
    comments = Comment.objects.filter(blog=blog)
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        # blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog=blog)
        comment.save()
    context={
        'blog': blog,
        'comments': comments,
        'EditBlogForm': EditBlogForm()
        }
    return render (request, "blog_details.html", context)

''' END of CRUD Blog '''


def contact_us(request):
    return render (request, "contact_us.html", context={})


# general functions 
def appointment(request):
    return render (request, "appointment.html", context={})

def directions(request):
    return render (request, "directions.html", context={})



# administration panel
def adminpanel(request):
    return render (request, "admin_panel.html", context={})




