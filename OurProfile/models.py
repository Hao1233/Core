from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Post(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    images = models.ImageField(null = True,blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Tag,null=True)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    customer_comment = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.body