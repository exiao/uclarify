__author__ = 'ericxiao'
from li_registration.models import UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def create_user_profile(sender, instance, created, **kwargs):
    """Get the temproray profile creating in the form class, then linked it to the user instance"""
    profile, created = UserProfile.objects.get_or_create(email=instance.email)
    profile.user = instance
    profile.save()

    user = profile.user
    user.first_name = profile.first_name
    user.last_name = profile.last_name
    user.save()

post_save.connect(create_user_profile, sender=User)