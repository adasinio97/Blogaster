from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
'''
class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
'''
'''class Author(models.Model):
    login=models.CharField(max_length=80,unique=True,default='uzytkownik',primary_key=True)
    name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    abc = models.CharField(max_length=50,default='haslo')
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    def __str__(self):
        return "%s %s (%s)" % (self.last_name,self.name, self.email)
'''


class BlogClass(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogi')
    created_date = models.DateTimeField(default=timezone.now,editable=False)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Post(models.Model):
    blog = models.ForeignKey('BlogClass', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posty')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now,editable=False)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def blog_p(self):
        return self.blog


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='komentarze')
    text=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    com = models.ForeignKey('self',on_delete=models.CASCADE,default=None,null=True,blank=True)

    def __str__(self):
        return self.text

    def children(self):
        return Comment.objects.filter(com=self)

    @property
    def is_parent(self):
        if self.com is not None:
            return False
        return True
