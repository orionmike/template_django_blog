
from django.core.management.base import BaseCommand
from faker import Faker
from filebrowser.fields import FileObject

from _generator_image.generate_set import generate_image_category
from _utils.utils import get_slug
from blog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Category.objects.all().delete()

        fake = Faker(['ru_RU'])

        count = 0

        for _ in range(10):

            category_name = f'Category {str(count+1).zfill(2)}'

            slug = get_slug(category_name)

            image_path = f'blog/category/{slug}/{slug}.webp'
            generate_image_category(image_path)

            Category.objects.create(
                title=category_name,
                preview_text=fake.paragraph(nb_sentences=1),
                full_text=fake.paragraph(nb_sentences=3),
                image=FileObject(image_path),
            )

            count += 1

        print(f'Category genereited: {count}')
