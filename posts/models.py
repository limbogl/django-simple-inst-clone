from django.db import models
from accounts.models import Profile
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200, null=True, blank=True)
    post_picture = models.ImageField(upload_to='posts/photos', null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} by @{}".format(self.post_title, self.profile)


