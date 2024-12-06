from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
