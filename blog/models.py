from django.db import models
from django.urls import reverse
from account.models import User
from django.utils.html import format_html
from django.utils import timezone
from extensions.utils import jalali_converter
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment




# my managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name="زیر دسته")
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="جایگاه")

    def __str__(self):
        return self.title
    objects = CategoryManager()




class Article(models.Model):
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ['-publish']

    STATUS_CHOICES = (
        ('d', 'پیش نویس'), # draft
        ('p', 'منتشر شده'), # publish
        ('i', 'درحال برسی'), # pennding
        ('b', 'برگشت داده شده'), # back
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    title = models.CharField(max_length=100,verbose_name='نام مقاله')
    description = models.TextField(verbose_name='متن مقاله')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
    thumbnail = models.ImageField(upload_to='ArticleImg', verbose_name='تصویر ')
    # timezone.now az library time zone be hamin alan eshare mikone yani vaghti ke article sakhte mishe
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    # auto_now_add yani zamani ke create shod mohem nist publish shode ya na zaman now ro add kon
    created = models.DateTimeField(auto_now_add=True)
    # auto_now yani be sorate auto zamani ke edit shode ro add kon
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت انشار')
    is_special = models.BooleanField(default=False, verbose_name="مقاله ویژه")
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField("IpAddress", through="ArticleHit", blank=True, related_name="hits", verbose_name="بازدید ها")

    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("account:home")
    # def convert_to_jalali(self):
    #     return datetime2jalali(self.publish)
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    
    def category_to_str(self):
        return "، ".join([category.title for category in self.category.active()])
    category_to_str.short_description = "دسته بندی "
    
    # def category_published(self):
    #     return self.category.filter(status=True)
    
    def thumbnail_tag(self):
        return format_html("<img width=100 height=70 style='border-radius:5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "تصویر مقاله"

    objects = ArticleManager()


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی پی")

class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IpAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


