from email import message
from django.contrib import admin
from .models import *

# Register your models here.
def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شدند"
    modeladmin.message_user(request, f"{rows_updated} مقاله {message_bit}")

make_published.short_description = 'منتشر کردن موارد انتخابی'


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "پیش نویس شد"
    else:
        message_bit = "پیش نویس شدند"
    modeladmin.message_user(request, f"{rows_updated} مقاله {message_bit}")
make_draft.short_description = 'پیش نویس کردن موارد انتخابی'


def make_active_category(modeladmin, request, queryset):
    rows_updated = queryset.update(status=True)
    if rows_updated == 1:
        message_bit = "دسته بندی فعال شد"
    else:
        message_bit = "دسته بندی فعال شد"
    modeladmin.message_user(request, f"{rows_updated} دسته بندی {message_bit}")
make_active_category.short_description = 'فعال کردن دسته بندی های انتخابی'


def make_deactive_category(modeladmin, request, queryset):
    rows_updated = queryset.update(status=False)
    if rows_updated == 1:
        message_bit = "دسته بندی غیر فعال شد"
    else:
        message_bit = "دسته بندی غیر فعال شد"
    modeladmin.message_user(request, f"{rows_updated} دسته بندی {message_bit}")
make_deactive_category.short_description = ' غیر فعال کردن دسته بندی های انتخابی'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_active_category, make_deactive_category]

class ArticleAdmin(admin.ModelAdmin):
    # baraye namayesh mohtava dar panel admin
    list_display = ('title', 'thumbnail_tag', 'slug', 'author', 'jpublish', 'is_special', 'status', 'category_to_str')
    # filter kardane maghalat bar asase publish va status
    list_filter = ('publish', 'status', 'author')
    # search kardan beyne data ha bar mabna title va description
    search_fields = ('title', 'description')
    # por kardane slug bar mabnaye title
    prepopulated_fields = {'slug': ('title',)}
    # ordering bar mabnaye status va publish
    ordering = ['-status', '-publish']
    actions = [make_published, make_draft]
   




admin.site.register(Article, ArticleAdmin)
admin.site.register(IpAddress)
admin.site.register(Category, CategoryAdmin)