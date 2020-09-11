from django.urls import path
from .views import Test

app_name = 'api'
urlpatterns = [
    path('test/', Test.as_view())
]
