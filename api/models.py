from django.db import models
import uuid

class User(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    realname = models.TextField()
    username = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField()

class Subscribe(models.Model):
    subscribe_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=100)
    following_email = models.CharField(max_length=100)

class Like(models.Model):
    like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=100)
    post_id = models.UUIDField()

class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    media = models.TextField()
    user_email = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.UUIDField()
    text = models.TextField()
    user_email = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rbr(models.Model):
    rbr_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reply_id = models.UUIDField()
    text = models.TextField()
    user_email = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
