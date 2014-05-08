from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=150, blank=True)
    job_title = models.CharField(max_length=150, blank=True)
    photo = ResizedImageField(max_width=1024, max_length=1024, upload_to='profile_images/', blank=True)
    alias = models.CharField(max_length=100, unique=True, null=True)

    def __unicode__(self):
        return u'Profile: %s' % self.email

    @property
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    # def save(self, *args, **kwargs):
    #     try:
    #         existing = UserProfile.objects.get(user=self.user)
    #         self.id = existing.id #force update instead of insert
    #     except UserProfile.DoesNotExist:
    #         pass
    #     models.Model.save(self, *args, **kwargs)

def social_auth_to_profile(backend, details, response, user=None, is_new=False, *args, **kwargs):
    if is_new:
        profile, created = UserProfile.objects.get_or_create(user=user)
    else:
        profile = UserProfile.objects.get(user=user)
    # Some of the default user details given in the pipeline
    profile.email = details['email']

    # Now we also need the extra details, found in the `social_user` kwarg
    social_user = kwargs['social']
    #import json
    #print(social_user.extra_data)
    #print(json.dumps(social_user.extra_data, indent=4, sort_keys=True))
    profile.company = social_user.extra_data['headline']
    profile.job_title = social_user.extra_data['positions']['values'][0]['title']
    profile.save()