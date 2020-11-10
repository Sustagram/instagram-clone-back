from django.urls import path
from .views import Register, Login, Me, PostAPI, Follow, MyPostAPI

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('me/', Me.as_view()),
    path('post/', PostAPI.as_view()),
    path('post/my/', MyPostAPI.as_view()),
    path('follow/', Follow.as_view())
]
