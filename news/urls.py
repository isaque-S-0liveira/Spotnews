# events/urls.py
from django.urls import path
from news.views import index, new_detail, category, new


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:new_id>/", new_detail, name="news-details-page"),
    path("categories/", category, name="categories-form"),
    path('news/', new, name='news-form')
]
