from django.db import models
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    email=models.EmailField(default="")
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    biography=models.TextField(help_text="Napisz coś o sobie",blank=True,null=True)

    def __str__(self):
        return 'Profil użytkownika: {}.'.format(self.user.username)
# Create your models here.
