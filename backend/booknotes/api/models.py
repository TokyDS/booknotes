import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    return "static/img/covers/{1}".format(instance.id,filename)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)
    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.pk)])

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название книги")
    description = models.TextField(blank=True, verbose_name="Описание")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    genre = models.ManyToManyField(Genre)
    reading_progress = models.IntegerField(default=0, null=False)
    last_opened = models.DateTimeField(auto_now=True)
    
    book = models.FileField(upload_to='books/%Y-%m-%d', blank=True, null=True, verbose_name="Книга")
    cover = models.ImageField(upload_to=user_directory_path, default='static/img/covers/default.jpg', verbose_name="Обложка")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.pk)])


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Conspect(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=2560)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.title
