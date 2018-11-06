from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateField('date published')
    image = models.ImageField("Cover (best ratio is 3:2)", upload_to='static/imgs/articles')

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=20)

    def __str__(self):
        return self.title

class Issue(models.Model):
    term = models.CharField(max_length=20)
    title =  models.CharField(max_length=20)
    date = models.DateField('date published')
    issu = models.CharField(max_length=80)
    image = models.ImageField("Cover (best ratio is 3:2)", upload_to='static/imgs/issues')

    def __str__(self):
        return self.term + ": " + self.title
