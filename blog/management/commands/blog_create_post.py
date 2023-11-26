
from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Category, Post, Tag
from filebrowser.fields import FileObject

from faker.providers import *

import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker(['ru_RU'])

        Post.objects.all().delete()

        category_list = Category.objects.all()
        cat_list_id = []
        for c in list(category_list):
            cat_list_id.append(c.id)

        print(cat_list_id)

        tag_list = list(Tag.objects.all())

        count = 0

        for index in range(90):

            random_category_id = random.choice(cat_list_id)
            # print(random_category_id)
            random_tags = random.sample(tag_list, 3)
            print(random_tags)

            ind = str(index + 1).zfill(2)
            # image = FileObject(f'blog/post-{ind}/post-{ind}.webp')

            post = Post.objects.create(
                title=f'Пост {ind}',

                category_id=int(random_category_id),
                preview_text=fake.paragraph(nb_sentences=2),
                full_text=fake.paragraph(nb_sentences=6),
                # image=image
            )
            post.tag_list.set(random_tags)
            post.save()
            count += 1

        print(f'Post list genereited: {count}')
