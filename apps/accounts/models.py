from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    name = models.CharField(default='', max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(default='', max_length=10)
    location = models.CharField(default='', max_length=50)
    GENDER_OPTIONS = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    gender = models.CharField(choices=GENDER_OPTIONS, default="Male", max_length=10)

    slug = models.SlugField(default='', unique=True)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.slug

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()