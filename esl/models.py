from datetime import datetime 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.reverse_related import ManyToOneRel
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tournament(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    event_name = models.TextField(max_length=40)
    game_name = models.TextField(max_length=40)
    created_date = models.DateTimeField(default=datetime.now)
    event_date = models.DateTimeField(default=datetime.now)
    register_count = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    city = models.TextField(max_length=50, blank=True)
    state = models.TextField(max_length=50, blank=True)
    country = models.TextField(max_length=50, blank=True)
    pin_code = models.IntegerField(default=000000, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    
class Result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)
    position = models.CharField(default=None, max_length=3)
    date = models.DateField(auto_now=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Result)
def hear_signal(sender , instance , **kwargs):
    print(instance.user,instance.event.creator,instance.position)
    tour = Tournament.objects.get(event_name=instance.event.event_name)
    tour.register_count+=1
    tour.save()
    #Do whatever you want. 
    #Your trigger function content.
    #Parameter "instance" will have access to all the attributes of the model being saved. To quote from docs : It's "The actual instance being saved."        

    return