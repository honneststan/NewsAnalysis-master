from django.contrib import admin
from .models import News, NewsVote, NewsComment


# Register your models here.
admin.site.register([News, NewsVote, NewsComment])

