from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to='author_pics', null=True, blank=True)
    short_title = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.short_title)



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='post_pics', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Section(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='section_pics', null=True, blank=True)

    def __str__(self):
        if self.title is None:
            return str(self.post) + ": ~~~" + str(self.body)[:20]
        else:
            return str(self.post) + ": " + str(self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user) + ":  " + str(self.body)[:15]
