from django.shortcuts import render, redirect
from app.models import Article
from app.forms import CreateArticleForm


def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles": articles})


def create_article(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            new_article = Article(
                title=form_data['title'],
                status=form_data['status'],
                content=form_data['content'],
                word_count=form_data['word_count'],
                twitter_post=form_data['twitter_post'],
            )
            new_article.save()
            return redirect('home')
    else:
        form = CreateArticleForm()
    return render(request, "app/article_create.html", {"form": form})
