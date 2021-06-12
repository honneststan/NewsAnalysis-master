from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateNewsForm, UpdateNewsForm, CreateCommentForm
from .models import News, NewsComment
from .webscrapers import baahrakhari_webscraping
from .webscrapers import ekantipur_webscraping
from .webscrapers import gorkhapatraonline_webscraping
from .webscrapers import onlinekhabar_webscraping
from .sentiment_analyzers import sentiment_intensity_analyzer
from .sentiment_analyzers import textblob_sentiment_analyzer
from .google_translation import google_translation
from .emotion_counter import emotion_counter

from reader.models import Reader

# Create your views here.
@login_required
def create_news(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateNewsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('news:read-news')
        else:
            form = CreateNewsForm()
        context = {
            'form': form
        }
        return render(request, "news/create.html", context)
    else:
        return redirect("news:read-news")


def read_news(request):
    newses = News.objects.all()
    context = {
        "newses": newses
    }
    return render(request, "news/read.html", context)

@login_required
def update_news(request, pk):
    if request.user.is_superuser:
        required_news = News.objects.get(id=pk)
        if request.method == 'POST':
            form = UpdateNewsForm(instance=required_news,data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('news:read-news')
        else:
            form = UpdateNewsForm(instance=required_news)
        context = {
            'form': form
        }
        return render(request, "news/update.html", context)
    else:
        return redirect("news:read-news")

@login_required
def delete_news(request, pk):
    if request.user.is_superuser:
        required_news = News.objects.get(id=pk)
        if request.method == "POST":
            required_news.delete()
            return redirect('news:read-news')
        return render(request, "news/delete.html")
    else:
        return redirect("news:read-news")


def view_news(request, pk):
    required_news = News.objects.get(id=pk)
    comments = NewsComment.objects.filter(news=required_news)
    if not request.user.is_superuser:
        required_reader = Reader.objects.get(user=request.user)
    converted_title = google_translation.ArticleConversion(required_news.title)
    converted_description = google_translation.ArticleConversion(required_news.description)
    emotions = emotion_counter.emotion_counter(str(converted_title) + (converted_description))
    emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
    emotions = dict(emotions)
    emotions_keys = list(emotions.keys())
    emotions_values = list(emotions.values())
    sia = sentiment_intensity_analyzer.sentiment_analyzer(converted_description)
    # tsa = textblob_sentiment_analyzer.textblob_sentiment_analyzer(converted_text)
    if request.method == 'POST' and not request.user.is_superuser:
        form = CreateCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = required_news
            comment.reader = required_reader
            comment.save()
            return redirect('news:view-news', pk=pk)
    else:
        form = CreateCommentForm()
    context = {
        "news": required_news,
        "converted_title": converted_title,
        "converted_description": converted_description,
        "positive": sia[0],
        "negative": sia[1],
        "neutral": sia[2],
        "polarity": sia[3],
        "comments": comments,
        "form": form,
        "emotions": emotions,
        "emotions_keys": emotions_keys,
        "emotions_values": emotions_values
    }
    return render(request, "news/view.html", context)


@login_required
def like_news(request, pk):
    required_news = News.objects.get(id=pk)
    if request.user not in required_news.likes.all():
        required_news.likes.add(request.user)
    else:
        required_news.likes.remove(request.user)
    return redirect('news:view-news', pk=required_news.id)


def webscrap_news(request):
    baahrakhari_newses = baahrakhari_webscraping.baahrakhari_list_webscraping()
    ekantipur_newses = ekantipur_webscraping.ekantipur_list_webscraping()
    gorkhapatraonline_newses = gorkhapatraonline_webscraping.gorkhapatraonline_list_webscraping()
    onlinekhabar_newses = onlinekhabar_webscraping.onlinekhabar_list_webscraping()
    newses = baahrakhari_newses + ekantipur_newses + gorkhapatraonline_newses + onlinekhabar_newses
    for news in newses:
        registered_news = News.objects.create(title=news[0], image=news[1], source=news[2], description=news[3])
        registered_news.save()
    registered_newses = News.objects.all()
    context ={
        "newses": registered_newses
    }
    return render(request, "news/webscrap.html", context)


