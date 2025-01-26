from django.urls import path
from . import views
# from app.views import home, create_article
from app.views import  CreateArticleView, ArticleListView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    # path('', home,name='home'),
    # path('articles/create/', create_article, name='create_article'),
    path('', ArticleListView.as_view(), name='home'),
    path('create/', CreateArticleView.as_view(), name='article_create'),
    path('<int:pk>/view/', views.article_view, name='article_view'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]