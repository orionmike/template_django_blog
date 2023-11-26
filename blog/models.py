
from datetime import datetime

from django.db import models
from django.urls import reverse
from filebrowser.fields import FileBrowseField

from _utils.utils import get_slug


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    is_publish = models.BooleanField(default=True)
    slug = models.CharField(max_length=150, blank=True, unique=True)
    preview_text = models.TextField(blank=True)
    full_text = models.TextField(blank=True)

    order = models.IntegerField(blank=True, default=100)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = get_slug(self.title)

        super().save(*args, **kwargs)

    def ___str__(self):
        return self.title

    def get_post_list(self):
        return Post.objects.filter(category_id=self.pk)

    def get_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse('category_update', kwargs={'slug': self.slug})

    # def get_delete_url(self):
    #     return reverse('category_delete', kwargs={'slug': self.slug})

    class Meta:
        db_table = "blog_category"
        ordering = ['-date_update']
        verbose_name = 'Блог: Категория'
        verbose_name_plural = 'Блог: Категории'


class Tag(models.Model):
    title = models.CharField(max_length=50)
    is_publish = models.BooleanField(default=True)
    slug = models.CharField(max_length=150, blank=True, unique=True)

    preview_text = models.TextField(blank=True)
    full_text = models.TextField(blank=True)

    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    def ___str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = get_slug(self.title)

        self.date_update = datetime.now()

        super().save(*args, **kwargs)

    # def get_posts(self):
    #     return Post.objects.filter(tag_list.contains)

    def get_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    # def get_delete_url(self):
    #     return reverse('tag_delete', kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse('tag_update', kwargs={'slug': self.slug})

    class Meta:
        db_table = "blog_tag"
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    is_publish = models.BooleanField(default=True)
    slug = models.CharField(max_length=150, blank=True, unique=True)

    keywords = models.CharField(max_length=250, blank=True)

    image = FileBrowseField(
        "Image", max_length=200, directory="media/work-list",
        extensions=[".webp", ".jpg", ".png"], blank=True, null=True,
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, default=1)
    tag_list = models.ManyToManyField('Tag', blank=True, related_name='post_list')

    preview_text = models.TextField(blank=True)
    full_text = models.TextField(blank=True)

    date_publish = models.DateTimeField(blank=True)

    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def ___str__(self):
        return f"{self.title}, {self.slug}"  # self.title

    def save(self, *args, **kwargs):

        self.slug = get_slug(self.title)

        if not self.date_publish:
            self.date_publish = datetime.now()

        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse('post_update', kwargs={'slug': self.slug})

    # def get_delete_url(self):
    #     return reverse('post_delete', kwargs={'slug': self.slug})

    class Meta:
        db_table = "blog_post"
        ordering = ['-date_publish']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
