from rest_framework import serializers

from .models import User, Post, Subscribe, Reply


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Subscribe


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Reply
