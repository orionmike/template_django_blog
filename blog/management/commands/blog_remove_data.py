
from django.core.management.base import BaseCommand
from blog.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Tag.objects.all().delete()
        Post.objects.all().delete()

        print(f'blog data remove')
