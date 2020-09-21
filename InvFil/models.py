from django.db import models
from django.conf import settings

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=settings.MEDIA_URL)

    def __str__(self):
        return self.title
