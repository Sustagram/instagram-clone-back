from django import forms


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()


class RegisterForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
    realname = forms.CharField()
    username = forms.CharField()


class PostForm(forms.Form):
    text = forms.CharField()
    media = forms.CharField()
    userId = forms.UUIDField()


class FollowForm(forms.Form):
    followingId = forms.UUIDField()


class ReplyForm(forms.Form):
    postId = forms.UUIDField()
    text = forms.CharField()
