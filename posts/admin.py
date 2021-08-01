from django.contrib import admin
from .models import Post
# Register your models here.

#class PostAdmin(admin.ModelAdmin):
#    
#    readonly_fields = ['profile', 'post_title', 'post_picture', 'date_created']
#
#admin.site.register(Post, PostAdmin)

admin.site.register(Post)
