from rest_framework import serializers
from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ['text', 'pub_date', 'author', 'image', 'group']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['title', 'slug', 'discription']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ['author', 'post', 'text', 'created']
        read_only_fields = ('post',)
