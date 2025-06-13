import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import About


# using dango signals to handle file deletion after deleting a post
@receiver(post_delete, sender=About)
def delete_files_on_instance_delete(sender, instance, **kwargs):
    if instance.logo1 and os.path.isfile(instance.logo1.path):
        os.remove(instance.logo1.path)
    if instance.logo2 and os.path.isfile(instance.logo2.path):
        os.remove(instance.logo2.path)
    if instance.side_image and os.path.isfile(instance.side_image.path):
        os.remove(instance.side_image.path)
