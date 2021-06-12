from django.urls import path
from .views import create_news, read_news, update_news, delete_news, view_news, like_news, webscrap_news

from config.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = "news"

urlpatterns = [
    path("create", create_news, name="create-news"),
    path("read", read_news, name="read-news"),
    path("update/<int:pk>", update_news, name="update-news"),
    path("delete/<int:pk>", delete_news, name="delete-news"),
    path("view/<int:pk>", view_news, name="view-news"),
    path("like/<int:pk>", like_news, name="like-news"),
    path("webscrap", webscrap_news, name="webscrap-news"),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
