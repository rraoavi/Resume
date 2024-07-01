from django.db import models

# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    education = models.TextField(max_length=5000)
    experience = models.TextField(max_length=5000)
    skills = models.TextField(max_length=5000)
    languages = models.CharField(max_length=500)
    projects = models.TextField(max_length=5000, default=None)
    # country = models.CharField(max_length=100,default=None, blank=True)
    state = models.CharField(max_length=100,default=None, blank=True)
    city = models.CharField(max_length=100,default=None, blank=True)
    block = models.CharField(max_length=200,default=None, blank=True)
    house_number = models.CharField(max_length=100,default=None, blank=True)

    def __str__(self):
        return self.name
