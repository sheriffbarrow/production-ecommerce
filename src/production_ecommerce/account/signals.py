from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserVendor


@receiver(post_save, sender=email)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserVendor.objects.create(user=instance)
        print("user profile created!!")


@receiver(post_save, sender=email)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()
    print("user profile save")
