# from django.conf import settings
from django.db import models
from embed_video.fields import EmbedVideoField
from django.shortcuts import reverse

# Create your models here.
# 

class Cpp(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("tutorial:course", kwargs={
            'slug': self.slug
        })


class C(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorial:course", kwargs={
            'slug': self.slug
        })

class Java(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = models.URLField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorial:course", kwargs={
            'slug': self.slug
        })


class JavaScript(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorial:course", kwargs={
            'slug': self.slug
        })


class Python(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorial:course", kwargs={
            'slug': self.slug
        })

class Php(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorial:course", kwargs={
            'slug': self.slug
        })