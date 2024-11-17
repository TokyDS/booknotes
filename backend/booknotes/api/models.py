from django.db import models
from django.urls import reverse

# Create your models here.
def user_directory_path(instance, filename): 
    return 'static/img/{0}/{1}'.format(instance.id, filename) 

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.pk)])
    
    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)    

class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.pk)])
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name    

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null= True)
    is_public = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    

class Conspect(models.Model):
    title = models.CharField()
    text = models.CharField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.title
        
