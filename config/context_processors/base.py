from _utils.request import CATEGORY_LIST, TAG_LIST
from config.config import SITE_TITLE


def object_list(request):
    return {
        'category_list': CATEGORY_LIST,
        'tag_list': TAG_LIST,
    }


def seo(request):
    return {
        'site_title': SITE_TITLE
    }
