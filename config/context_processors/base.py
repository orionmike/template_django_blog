from _utils.request import CATEGORY_LIST
from config.config import SITE_TITLE


def category_list(request):
    return {
        'category_list': CATEGORY_LIST,
    }


def seo(request):
    return {
        'site_title': SITE_TITLE
    }
