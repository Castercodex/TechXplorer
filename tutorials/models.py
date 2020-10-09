from django.db import models

# Create your models here.
class Cpp(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    

class C(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Java(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title


class JavaScript(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Python(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Php(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title