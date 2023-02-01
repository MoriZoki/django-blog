from django.urls import path
from .views import ArticleList, ArticleDetail, CategoryList, AuthorList, ArticlePre

app_name = 'blog'
urlpatterns = [
    # default url
    path('', ArticleList.as_view(), name='home'),
    # url with page id request
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='detail'),
    path('preview/<int:pk>', ArticlePre.as_view(), name='preview'),
    # default url
    path('category/<slug:slug>', CategoryList.as_view(), name='category'),
    # url with page id request
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='category'),
    path('author/<slug:username>', AuthorList.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author'),

]
