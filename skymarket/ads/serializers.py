from rest_framework import serializers

from ads.models import Ad, Comment
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.URLField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'author', 'created_at', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=100, read_only=True)
    author_last_name = serializers.CharField(max_length=100, read_only=True)
    phone = serializers.CharField(max_length=20, read_only=True)

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'author', 'created_at', 'description', 'author_first_name',
                  'author_last_name', 'phone']

