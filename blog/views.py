from account.models import User
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Article, Category
from django.core.paginator import Paginator
from account.mixins import AuthoAccessMixin


# Create your views here.

# def home(request, page=1):
#     # start code for pagination
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 4)
#     articles = paginator.get_page(page)
#     # end code for pagination
#     context = {
#         'article': articles,
#     }
#     return render(request, 'blog/home.html', context)
class ArticleList(ListView):
    # model = Article
    # template_name = 'blog/home.html'
    queryset = Article.objects.published()
    paginate_by = 4





# def detail(request, slug):
#         # try:
#         #     article = Article.objects.get(slug=slug)
#         # except Exception as e:
#         #     raise Http404
#     context = {
#         'single': get_object_or_404(Article.objects.published(), slug=slug)
#     }
#     return render(request, 'blog/detail.html', context)
class ArticleDetail(DetailView):
    template_name = 'blog/detail.html'
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
             article.hits.add(ip_address)
        return article


class ArticlePre(AuthoAccessMixin, DetailView):
    template_name = 'blog/detail.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)





# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()

#     paginator = Paginator(articles_list, 4)
#     articles = paginator.get_page(page)
#     context = {
#         "category": category,
#         "article": articles,
#     }
#     return render(request, 'blog/category.html', context)
class CategoryList(ListView):
    template_name = "blog/category.html"
    paginate_by = 5
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    template_name = "blog/author.html"
    paginate_by = 5
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
