
from django.shortcuts import get_object_or_404, render

from _utils.utils import get_pagination
from config.config import PAGINATE_BY

from .models import Category, Post, Tag


def search_post_list(request):

    search = request.GET.get('search', '')

    if search:
        post_list = Post.objects.filter(title__icontains=search, is_publish=True)
        object_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, post_list, PAGINATE_BY)

    else:
        post_list = Post.objects.filter(is_publish=True)
        object_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, post_list, PAGINATE_BY)

    return render(
        request,
        'blog/post_list.html',
        context={
            'object_list': object_list,
            'is_paginated': is_paginated,
            'next_page': next_url,
            'prev_page': prev_url,
        })


def post_list(request):

    post_list = Post.objects.filter(is_publish=True)
    object_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, post_list, PAGINATE_BY)

    return render(
        request,
        'blog/post_list.html',
        context={
            'object_list': object_list,
            'is_paginated': is_paginated,
            'next_page': next_url,
            'prev_page': prev_url,
        })


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    post_next = Post.objects.filter(date_update__gt=post.date_update).order_by('date_update').first()
    post_previos = Post.objects.filter(date_update__lt=post.date_update).order_by('-date_update').first()

    related_post_list = Post.objects.filter(
        is_publish=True,
        category_id=post.category).order_by('?').exclude(pk=post.pk)[:6]

    return render(
        request,
        'blog/post_detail.html',
        context={
            'post': post,

            'post_next': post_next,
            'post_previos': post_previos,

            'related_post_list': related_post_list
        })


def category_detail(request, slug):

    category = Category.objects.filter(slug=slug).first()

    post_list = Post.objects.filter(category_id=category.id).all()
    object_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, post_list, PAGINATE_BY)

    return render(
        request,
        'blog/category_detail.html',
        context={
            'category': category,
            'object_list': object_list,
            'is_paginated': is_paginated,
            'next_page': next_url,
            'prev_page': prev_url,
        })


def tag_detail(request, slug):

    tag = Tag.objects.filter(slug=slug).first()

    # post_list = Post.objects.filter(tag_list_set.contains(tag)).all()
    post_list = tag.post_list.all()
    object_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, post_list, PAGINATE_BY)

    print(object_list)

    return render(
        request,
        'blog/tag_detail.html',
        context={
            'tag': tag,
            'object_list': object_list,
            'is_paginated': is_paginated,
            'next_page': next_url,
            'prev_page': prev_url,
        })
