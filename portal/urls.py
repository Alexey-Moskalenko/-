from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list),
    path('post/<str:slug>/', competition_detail, name='competition_detail_url')
]