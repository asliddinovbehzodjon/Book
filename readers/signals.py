from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
@receiver(post_save, sender=User)
def kitobxon_updated(sender, instance, created, **kwargs):
    if not created:
        name = instance.username
        user = instance
        kitobxon=Kitobxon.objects.filter(user=user).update(name=name)
@receiver(post_save,sender=User)
def kitobxon_create(sender,instance,created,**kwargs):
    if created:
        user=instance
        if  instance.username:
              name = instance.username
        else:
             name = "Kitobxon"
        kitobxon=Kitobxon.objects.create(user=user,name=name)

@receiver(post_delete,sender=Kitobxon)
def kitobxon_delete(sender,instance,**kwargs):
    user=instance.user
    user.delete()