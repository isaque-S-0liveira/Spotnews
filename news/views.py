from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from news.models.news_model import News, Categories
from news.forms import CreateCategoriesForm, CreateNewsModelForm


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


def category(request):
    form = CreateCategoriesForm()
    context = {"form": form}
    if request.method == "POST":
        form = CreateCategoriesForm(request.POST)
        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")

    return render(request, "categories_form.html", context)


def new(request):
    form = CreateNewsModelForm()

    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)
        if form.is_valid():
            news_instance = News.objects.create(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                author=form.cleaned_data["author"],
                created_at=form.cleaned_data["created_at"],
                image=form.cleaned_data["image"],
            )
            news_instance.categories.set(form.cleaned_data["categories"])
            return redirect("home-page")

    context = {"form": form}
    return render(request, "news_form.html", context)
