from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Home, Global, Reservation, Service, ServiceCat, Team, Staff, Category, Contact_us, BlogPost, Comment, FAQCategory, FAQ, FAQComment

# Register your models here.
class HomeAdmin(ImportExportModelAdmin):
    list_display = ('content', )
    list_filter = ("created_on",)
    search_fields = ['content', ]

class GlobalAdmin(ImportExportModelAdmin):
    list_display = (
        'address', 
        'telephone', 
        'email', 
        'navermap', 
        'email', 
        'updated_on', 
        'created_on')
    list_filter = ("created_on",)
    search_fields = ['address', 'telephone', 'email',]
    
class ServiceAdmin(ImportExportModelAdmin):
    list_display = (
        'title', 
        'image', 
        'short', 
        'category', 
        'author', 
        # 'content', 
        'updated_on', 
        'created_on')
    list_filter = ("created_on",)
    search_fields = ['title', 'content', 'short',]

class ServiceCatAdmin(ImportExportModelAdmin):
    list_display = ('title', )
    list_filter = ("title",)
    search_fields = ['title', ]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class BlogPostAdmin(ImportExportModelAdmin):
    list_display = (
        'title', 
        'category', 
        'author', 
        'short', 
        # 'content', 
        'image', 
        'dateTime')
    list_filter = ("dateTime",)
    search_fields = ['title', 'short', 'author', 'content']
    # raw_id_fields = ('user',)
    # date_hierarchy = 'created_on'
    # ordering = ('status', 'created_on')
    
class CommentAdmin(ImportExportModelAdmin):
    list_display = (
        'user', 
        'content', 
        'blog', 
        'parent_comment', 
        'dateTime')
    list_filter = ("dateTime",)
    search_fields = ['content']
    # raw_id_fields = ('user',)
    # date_hierarchy = 'created_on'
    # ordering = ('status', 'created_on')    
    
class TeamAdmin(ImportExportModelAdmin):
    list_display = ('description', 'image')
    list_filter = ("description",)
    search_fields = ['description']
    
class StaffAdmin(ImportExportModelAdmin):
    list_display = (
        'name',
        'speciality',
        'staff',
        # 'bio',
        'updated_on',
        'created_on',
        'image')
    list_filter = ("name",)
    search_fields = ['name']

class ContactUsAdmin(ImportExportModelAdmin):
    list_display = (
        'title',
        'updated_on',
        'created_on')
    list_filter = ("title",)
    search_fields = ['title']

class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class FAQAdmin(ImportExportModelAdmin):
    list_display = (
        'title', 
        'category', 
        'author', 
        'is_read', 
        'status', 
        # 'content', 
        'dateTime')
    list_filter = ("is_read",)
    search_fields = ['title', 'content', 'author', 'category']
    # raw_id_fields = ('user',)
    # date_hierarchy = 'created_on'
    # ordering = ('status', 'created_on')
    
class FAQCommentAdmin(ImportExportModelAdmin):
    list_display = (
        'user', 
        'content', 
        'blog', 
        'dateTime')
    list_filter = ("dateTime",)
    search_fields = ['content']
    # raw_id_fields = ('user',)
    # date_hierarchy = 'created_on'
    # ordering = ('status', 'created_on')  
    
class ReservationAdmin(ImportExportModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone',
        'email',
        'reservation',
        'status',
        'created_on',
        'birthday',
        'note',)
    list_filter = ("created_on",)
    search_fields = ['first_name', 'last_name']

admin.site.register(FAQCategory, FAQCategoryAdmin)    
admin.site.register(FAQ, FAQAdmin)
admin.site.register(FAQComment, FAQCommentAdmin)
admin.site.register(Category, CategoryAdmin)    
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Contact_us, ContactUsAdmin)
admin.site.register(Global, GlobalAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCat, ServiceCatAdmin)