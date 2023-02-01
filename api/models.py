from django.db import models
from blog.models import Article
from account.models import User
# Create your models here.
class ApiArticle(Article):
    class Meta:
        ordering = ('-created',)


class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']