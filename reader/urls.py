from django.urls import path

from config.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import update_profile, view_profile
app_name = "reader"

urlpatterns = [
    path("update", update_profile, name="update-reader"),
    path("view", view_profile, name="view-reader"),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()