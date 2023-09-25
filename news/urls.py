# events/urls.py
from django.urls import path
from news.views import index, new_detail


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:new_id>", new_detail, name="news-details-page"),
]
