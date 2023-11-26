from django.urls import path

from .views import *


urlpatterns = [
    path('', post_list, name='post_list'),
    path('search/', search_post_list, name='search_post_list'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('c/<slug:slug>/', category_detail, name='category_detail'),
    path('t/<slug:slug>/', tag_detail, name='tag_detail'),
]
