from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('tweet/<int:id>/', views.tweet_detail_view),
]