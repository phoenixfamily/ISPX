import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Product


@receiver(pre_delete, sender=Product)
def delete_files_on_instance_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            print(f"Deleted {instance.image.path}")
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)
            print(f"Deleted {instance.video.path}")
