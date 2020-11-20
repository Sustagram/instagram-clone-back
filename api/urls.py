from django.urls import path
from .routes import auth, post, follow

urlpatterns = [
    path('register/', auth.Register.as_view()),
    path('login/', auth.Login.as_view()),
    path('me/', auth.Me.as_view()),
    path('post/', post.PostAPI.as_view()),
    path('post/my/', post.MyPostAPI.as_view()),
    path('follow/', follow.Follow.as_view())
]
