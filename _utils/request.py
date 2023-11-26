from blog.models import Category

CATEGORY_LIST = Category.objects.filter(is_publish=True).order_by('title')
