from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    about = models.TextField()


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=500)
    duration_months = models.IntegerField()
    price = models.FloatField()
    teacher = models.ManyToManyField(Teacher)


class Student(models.Model):
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)
