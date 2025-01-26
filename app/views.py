from typing import Any
import time
from django.shortcuts import render, redirect
from app.models import Article
from django.contrib.messages.views import SuccessMessageMixin
from app.forms import CreateArticleForm
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# def home(request):
#     articles = Article.objects.all()
#     # objects to manager do zapytan do bazy danych
#     return render(request, 'app/home.html', {'articles': articles})
#     # 'articles' - pod taka nazwa bedzie dostepna w html

# Function base view
# def create_article(request):
    # if request.method == 'POST':
    #     form = CreateArticleForm(request.POST)
    #     if form.is_valid():
    #         form_data = form.cleaned_data
    #         new_article = Article(
    #             title = form_data['title'],
    #             status = form_data['status'],
    #             content = form_data['content'],
    #             word_count = form_data['word_count'],
    #             twitter_post = form_data['twitter_post'],
    #         )
    #         new_article.save()
    #         return redirect('home')
    # else:
    #     form = CreateArticleForm()
    # return render(request, 'app/article_create.html', {'form': form})
# Create your views here.

# Class base view

class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'app/home.html'
    model = Article
    context_object_name = 'articles' 
    paginate_by = 5
    # articles - pod taka nazwa bedzie dostepna w html
    def get_queryset(self):
        time.sleep(2)
        search = self.request.GET.get('search')
        queryset = super().get_queryset().filter(creator=self.request.user)
        if search:
            queryset = queryset.filter(title__search=search)
        return queryset.order_by('-created_at')    


class CreateArticleView(LoginRequiredMixin, CreateView):
    template_name = 'app/article_create.html'
    model = Article
    fields = ('title', 'status', 'content', 'twitter_post')
    success_url = reverse_lazy('home')
    # wbudowana funkcja form_valid to validacja danych
    def form_valid(self, form):
        form.instance.creator = self.request.user
        # form.instance to inaczej obiekt artykulu
        return super().form_valid(form)
    # success_url - sciezka do ktorej zostanie przekierowany po zapisaniu artykulu
class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    template_name = 'app/article_update.html'
    model = Article
    fields = ('title', 'status', 'content', 'twitter_post')
    success_url = reverse_lazy('home')
    context_object_name = 'article'
    def test_func(self):
        return self.request.user == self.get_object().creator

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    template_name = 'app/article_delete.html'
    model = Article
    success_url = reverse_lazy('home')  
    # success_message = 'Article deleted successfully'
    context_object_name = 'article'
    def test_func(self):
        return self.request.user == self.get_object().creator
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Article deleted successfully', extra_tags='destructive')
        return super.post(request, *args, **kwargs)