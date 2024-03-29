from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
    
def createProfile(sender,instance,created,**kwargs):
    if created :
        user = instance
        profile= Profile.objects.create(
            user= instance,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

        subject = 'Welcome to devsearch'
        message_body = 'we are happy to see you!'
    
        send_mail(
            subject,
            message_body,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )




def deleteUser(sender,instance,**kwargs):
    user = instance.user
    user.delete()
    print('deleting user...')

post_save.connect(createProfile,sender=User)


post_delete.connect(deleteUser,sender=Profile)
