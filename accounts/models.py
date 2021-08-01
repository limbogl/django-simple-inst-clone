from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, unique=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='users/pictures', default='static/images/default-profile.png', null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name


    def save(self, force_insert=False, force_update=False, using=None,
                 update_fields=None):
            super().save()

            img = Image.open(self.profile_pic.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_pic.path)