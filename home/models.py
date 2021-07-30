from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.shortcuts import reverse
# from .utils import get_random_code
from django.template.defaultfilters import slugify
from django.db.models import Q


class Category(models.Model):
    category = models.CharField(max_length=1000)
    cat_img = models.ImageField(upload_to="shop/cats")
    cat1 = models.CharField(max_length=1000)
    cat2 = models.CharField(max_length=2000)
    cat3 = models.CharField(max_length=9000)
    cat4 = models.CharField(max_length=9000)
    cat5 = models.CharField(max_length=9000)

    def __str__(self):
        return f"Category of {self.category}"


class ShareitsUser(models.Model):
    Username = models.CharField(max_length=50)
    Userfriends = models.ManyToManyField(
        User, blank=True, related_name='friends')
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    bgimg = models.ImageField(upload_to='shop/bg', default="0")
    image = models.ImageField(upload_to='shop/userimg', default="1")
    updated = models.DateTimeField(auto_now=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.Username + " Sing up these : " + self.email


class Video(models.Model):
    Video_id = models.AutoField(primary_key=True)
    Video_url = models.FileField(
        upload_to="video/Videos", default="", max_length=5000)
    Video_name = models.CharField(max_length=5000)
    views = models.IntegerField(default=0)
    Category = models.CharField(max_length=5000, default="")
    Desc = models.CharField(max_length=9000)
    Tages = models.CharField(max_length=5000, default="")
    timestamp = models.DateTimeField(default=now)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.Video_name


