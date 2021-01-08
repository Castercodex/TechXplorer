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
    course_number = models.IntegerField(default=0)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorials:cpp", kwargs={
            'slug': self.slug
        })

    


class C(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()
    course_number = models.IntegerField(default=0)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorials:c", kwargs={
            'slug': self.slug
        })



class Java(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = models.URLField(blank=True)
    slug = models.SlugField()
    course_number = models.IntegerField(default=0)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorials:java", kwargs={
            'slug': self.slug
        })


class JavaScript(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()
    course_number = models.IntegerField(default=0)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorials:js", kwargs={
            'slug': self.slug
        })



class Python(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()
    course_number = models.IntegerField(default=0)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorials:python", kwargs={
            'slug': self.slug
        })

class Php(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    video_url = EmbedVideoField(blank=True)
    slug = models.SlugField()
    course_number = models.IntegerField(default=0)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorials:php", kwargs={
            'slug': self.slug
        })


 