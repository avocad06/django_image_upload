from django.db import models
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to="images/", blank=True)