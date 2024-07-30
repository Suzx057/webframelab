from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=100)
    videos = models.ManyToManyField(Video)

    def __str__(self):
        return self.name