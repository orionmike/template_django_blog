from django.urls import path

from .views import *


urlpatterns = [
    path('', post_list, name='post_list'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('b/<slug:slug>/', category_detail, name='category_detail'),
]
