from django.urls import path
# from app.views import home, create_article
from app.views import ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleListView

urlpatterns = [
    # path("", home, name="home"),
    # path("article/create/", create_article, name="create_article")
    path('', ArticleListView.as_view(), name="home"),
    path("create/", ArticleCreateView.as_view(), name="create_article"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="update_article"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete_article")
]
