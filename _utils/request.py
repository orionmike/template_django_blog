from catalog.models import ProductCategory

CATEGORY_LIST = ProductCategory.objects.filter(is_publish=True).order_by('title')
