from blog.models import Category, Tag

CATEGORY_LIST = Category.objects.filter(is_publish=True).order_by('title')
TAG_LIST = Tag.objects.filter(is_publish=True).order_by('title')
