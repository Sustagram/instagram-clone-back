import uuid

from django.db import models


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=100, unique=True)
    realname = models.TextField()
    username = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField()

    class Meta:
        db_table = "User"


class Subscribe(models.Model):
    subscribe_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id_set", db_column="user_id")
    following_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following_id_set", db_column="following_id")

    class Meta:
        db_table = "Subscribe"


class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    media = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Post"


class Like(models.Model):
    like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    post_id = models.OneToOneField(Post, on_delete=models.CASCADE, db_column="post_id")

    class Meta:
        db_table = "Like"


class Reply(models.Model):
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, db_column="post_id")
    text = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Reply"


class Rbr(models.Model):
    rbr_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reply_id = models.ForeignKey(Reply, on_delete=models.CASCADE, db_column="reply_id")
    text = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Rbr"
