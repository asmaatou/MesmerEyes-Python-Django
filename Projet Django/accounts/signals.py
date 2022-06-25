from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import User,Group


@receiver(post_save, sender=User)
def create_profil(sender,instance,created,**kwargs):
    if created :
        if instance.is_superuser :
            group=Group.objects.get(name='admin')
            instance.groups.add(group) 
            Admin.objects.create(
                user=instance
            )
            print('Profile created')
        else:
            group=Group.objects.get(name='customers')
            instance.groups.add(group)
            Customer.objects.create(
                user=instance,
                name=str(instance.first_name+" "+instance.last_name),
                email=instance.email,
                )
            print('Profile created')
post_save.connect(create_profil,sender=User)
