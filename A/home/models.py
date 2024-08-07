from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='qusers')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    # image = models.ImageField(upload_to='media',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # first 20
        return self.body[:20]


class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ausers")
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='aquestion')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)