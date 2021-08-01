from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Profile

def user_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='user')
		instance.groups.add(group)
		Profile.objects.create(
			user=instance,
			name=instance.username,
			)


def updateUser(sender, instance, created, **kwargs):
	profile = instance
	user = profile.user

	if created == False:
		user.username = profile.name
		user.email = profile.email
		user.description = profile.description
		user.save()



def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass



post_save.connect(user_profile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)