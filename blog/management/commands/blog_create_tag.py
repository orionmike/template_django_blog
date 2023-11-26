

from django.core.management.base import BaseCommand
from blog.models import Tag

from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Tag.objects.all().delete()

        fake = Faker(['ru_RU'])

        count = 0

        for _ in range(20):

            name = f'Tag {str(count+1).zfill(2)}'

            Tag.objects.create(
                title=name,
                preview_text=fake.paragraph(nb_sentences=1),
                full_text=fake.paragraph(nb_sentences=3),
            )

            count += 1

        print(f'Tag genereited: {count}')
