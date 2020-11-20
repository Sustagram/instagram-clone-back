from django.urls import path
from .routes import auth, post, follow, reply

urlpatterns = [
    path('register/', auth.Register.as_view()),
    path('login/', auth.Login.as_view()),
    path('me/', auth.Me.as_view()),
    path('user/<str:user_id>', auth.GetUser.as_view()),

    path('post/follow/', post.PostAPI.as_view()),
    path('post/my/', post.MyPostAPI.as_view()),

    path('follow/<str:follow_id>', follow.Follow.as_view()),
    path('follow/', follow.Follow.as_view()),

    path('reply/<str:post_id>', reply.ReplyAPI.as_view()),
    path('reply/', reply.ReplyAPI.as_view()),
]
