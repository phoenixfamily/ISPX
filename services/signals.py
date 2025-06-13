import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Services


@receiver(pre_delete, sender=Services)
def delete_files_on_instance_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            print(f"Deleted {instance.image.path}")

