from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Svg(models.Model):
    name = models.CharField(max_length=50, null=True)
    svg = models.FileField(upload_to="illustrations/svg", null=True)
    png = models.FileField(upload_to="illustrations/png", null=True)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.name
