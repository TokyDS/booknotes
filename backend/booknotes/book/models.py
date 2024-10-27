from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.__str__()    

# class Genre(models.Model):


class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title