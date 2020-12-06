from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    When default User model creates new instnance 
    this function creates new Profile model intance and automatic binds them.
    """
    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    """
    When default User model updates exist instnance 
    this function updates binded Profile model.
    """
    if created == False:
        instance.profile.save()
        print('Profile updated!')