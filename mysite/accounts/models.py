from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.user.username)

@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)