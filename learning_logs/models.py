from django.db import models
from datetime import date



# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    """Some specific learning about a topic"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    text = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text



class Entr(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
