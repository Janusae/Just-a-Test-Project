from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField
# Create your models here.
class User(AbstractUser):
    email_code = models.CharField(max_length=50 , unique=True)
    def __str__(self):
        if self.first_name and self.last_name :
            return f"{self.first_name} {self.last_name}"
        else :
            return f"{self.email}"



class User_plus(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    avatar = ResizedImageField(size=[300,300] , upload_to = 'avatars' , null=True , blank=True)
    about_user = models.TextField(null=True)
    def __str__(self):
        return f'{self.user}'

