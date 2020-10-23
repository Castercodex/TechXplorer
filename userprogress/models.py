from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=4)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.name


class EnrolledCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")

    def __str__(self):
        return self.user.username

class CompletedCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(EnrolledCourse)
    start_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
