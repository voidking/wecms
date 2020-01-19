from django.urls import path
from . import views
from . import views_wechat
from werobot.contrib.django import make_view

urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('wechat/',make_view(views_wechat.robot)),
]