# authors/models.py

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    video_title = models.CharField(max_length=200, blank=True, null=True)  # เพิ่มฟิลด์ video_title

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.video_title}'