from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from reader.models import Reader


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/news/")
    tags = models.TextField(null=True, blank=True, help_text="Write in tag1, Tag2, format")
    likes = models.ManyToManyField(User, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    news_instance = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return str(self.title)


class NewsComment(models.Model):
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/news/comments/")
    file = models.FileField(null=True, blank=True, upload_to="files/news/comments/")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_instance = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.id)


class NewsVote(models.Model):
    CHOICES = (
        ('Up', 'Up'),
        ('Down', 'Down')
    )
    vote = models.CharField(max_length=255, choices=CHOICES, null=True, blank=True)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    vote_instance = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.id)


