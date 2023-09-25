from django.shortcuts import render, get_object_or_404
from django.http import Http404
from news.models.news_model import News


def index(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def new_detail(request, new_id):
    try:
        context = get_object_or_404(News, id=new_id)
        return render(
            request,
            "news_details.html",
            {"new": context, "categories": context.categories.all()},
        )
    except Http404:
        return render(request, "404.html")
