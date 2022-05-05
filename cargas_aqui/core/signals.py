from .models import Cargo, CargoStatusChange
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

@receiver(pre_save, sender = Cargo)
def model_pre_save(sender, instance, **kwargs):
    try:
        instance._pre_save_status =  Cargo.objects.get(pk=instance.pk).status
    except Cargo.DoesNotExist:
        instance._pre_save_status = instance.status


@receiver(signal=post_save, sender = Cargo)
def model_post_save(sender, instance, created, **kwargs):
    if instance._pre_save_status != instance.status:
        CargoStatusChange.objects.create(
            cargo = instance,
            old_status = instance._pre_save_status,
            new_status = instance.status
        )