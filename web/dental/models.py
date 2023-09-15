from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.urls import reverse
from autoslug import AutoSlugField
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


# clinic dentists team testimonials services service_details gallery blog blog_details contact_us appointments directions

class Global(models.Model):
    address = 
    telephone = 
    


class Category(models.Model):
    title = models.CharField(max_length=255)


class BlogPost(models.Model):
    title=models.CharField(max_length=255)
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
    dateTime=models.DateTimeField(default=now)

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