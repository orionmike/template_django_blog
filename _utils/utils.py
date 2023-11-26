from pathlib import Path

from django.core.paginator import Paginator
from slugify import slugify

from config.settings import BASE_DIR


def get_slug(line_string: str) -> str:
    line_string = line_string.replace('й', 'j')
    result = slugify(line_string)
    result = result.replace('ja', 'ya')
    result = result.replace('ia', 'ya')
    print(result)
    return result


def get_pagination(request, object_list, paginate_by) -> tuple:

    paginator = Paginator(object_list, paginate_by)
    page_number = request.GET.get('page', 1)
    page_object_list = paginator.get_page(page_number)
    is_paginated = page_object_list.has_other_pages()

    print(page_number)

    if page_object_list.has_previous():
        prev_url = f'?page={page_object_list.previous_page_number()}'
    else:
        prev_url = ''

    if page_object_list.has_next():
        next_url = f'?page={page_object_list.next_page_number()}'
    else:
        next_url = ''

    return page_object_list, paginator, is_paginated, prev_url, next_url


def get_foto_list(obj) -> list:

    image_dir = Path(str(obj.image)).parent
    abs_work_dir = BASE_DIR / 'media' / image_dir / 'foto'

    image_list = []
    image_path_list = list(abs_work_dir.glob('**/*.*'))
    for img in image_path_list:
        if img.suffix in ['.webp', '.jpg']:
            image_list.append(f'/media/{image_dir.parent.name}/{image_dir.name}/foto/{img.name}')

    image_list.sort()

    return image_list
