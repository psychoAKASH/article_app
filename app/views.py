from django.shortcuts import render
from app.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles": articles})
