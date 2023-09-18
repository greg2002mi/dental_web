from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.urls import reverse
from autoslug import AutoSlugField
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

STATUS = (
    (0,"Applied"),
    (1,"Processing"),
    (2,"Closed")
)

# Create your models here.

class Home(models.Model):
    content = CKEditor5Field('Content', config_name='extends', blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
# clinic dentists team testimonials services service_details gallery blog blog_details contact_us appointments directions

class Global(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=False, blank=True, null=True)
    navermap = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # schedule_weekday = models.CharField(max_length=255) # something like 
    # schedule_start = models.CharField(max_length=255)
    # schedule_end = models.CharField(max_length=255)
    # schedule_lunch = models.CharField(max_length=255)

# gallery
class Gallery(models.Model):
    title = models.CharField(max_length=150)
    filename = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)

# reservation
class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(_("email address"), unique=False, blank=True, null=True)
    reservation = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField(blank=True, null=True)
    note = models.TextField()

    
# services    

class Service(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    short = models.TextField()

class ServiceDetails(models.Model):
    category = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='details')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = CKEditor5Field('Content', config_name='extends', blank=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
# team
class Team(models.Model):
    description = CKEditor5Field('Content', config_name='extends', blank=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)

class Staff(models.Model):
    name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    bio = CKEditor5Field('Content', config_name='extends', blank=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
       
# blog    

class Category(models.Model):
    title = models.CharField(max_length=255)

class Contact_us(models.Model):
    title = CKEditor5Field('Content', config_name='extends', blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog')
    author= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug=AutoSlugField(populate_from='title')
    short = models.TextField()
    content=CKEditor5Field('Content', config_name='extends', blank=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author.first_name) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')
    
    @property
    def is_sorted(self):
        if self.category is None:
            return True
        return False
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    dateTime=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=['-dateTime']    

    def __str__(self):
        return self.user.first_name +  " Comment: " + self.content
    
    @property
    def children(self):
        return Comment.objects.filter(parent_comment=self).reverse()
    
    @property
    def is_parent(self):
        if self.parent_comment is None:
            return True
        return False

# FAQ sector

class FAQCategory(models.Model):
    title = models.CharField(max_length=255)
    
class FAQ(models.Model):
    title=models.CharField(max_length=255)
    category = models.ForeignKey(FAQCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='FAQ')
    author= models.CharField(max_length=255)
    slug=AutoSlugField(populate_from='title')
    content = models.TextField()
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    @property
    def is_sorted(self):
        if self.category is None:
            return True
        return False
    
class FAQComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    dateTime=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=['-dateTime']    

    def __str__(self):
        return self.user.first_name +  " Comment: " + self.content