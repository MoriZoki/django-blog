from rest_framework import serializers
from .models import ApiArticle


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiArticle
        fields = ['id', 'title', 'url', 'poster', 'created']