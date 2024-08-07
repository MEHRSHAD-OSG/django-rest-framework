from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#
#     address = models.CharField(max_length=200)
#     phone_number = models.CharField(max_length=11,unique=True)
#
#     USERNAME_FIELD = 'username'
#     objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User,models.CASCADE,related_name='uprofile')
    age = models.PositiveSmallIntegerField(default=1)
    bio = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='media/',null=True,blank=True)

    def __str__(self):
        return f'{self.user} _ {self.bio}'