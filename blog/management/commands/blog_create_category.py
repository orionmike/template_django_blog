

from django.core.management.base import BaseCommand
from blog.models import Category

from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Category.objects.all().delete()

        fake = Faker(['ru_RU'])

        count = 0

        for _ in range(10):

            name = f'Category {str(count+1).zfill(2)}'

            Category.objects.create(
                title=name,
                preview_text=fake.paragraph(nb_sentences=1),
                full_text=fake.paragraph(nb_sentences=3),
            )

            count += 1

        print(f'Category genereited: {count}')
