# Generated by Django 4.2.6 on 2023-11-26 10:49

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('is_publish', models.BooleanField(default=True)),
                ('slug', models.CharField(blank=True, max_length=150, unique=True)),
                ('preview_text', models.TextField(blank=True)),
                ('full_text', models.TextField(blank=True)),
                ('order', models.IntegerField(blank=True, default=100)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Блог: Категория',
                'verbose_name_plural': 'Блог: Категории',
                'db_table': 'blog_category',
                'ordering': ['-date_update'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_publish', models.BooleanField(default=True)),
                ('slug', models.CharField(blank=True, max_length=150, unique=True)),
                ('preview_text', models.TextField(blank=True)),
                ('full_text', models.TextField(blank=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'db_table': 'blog_tag',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('is_publish', models.BooleanField(default=True)),
                ('slug', models.CharField(blank=True, max_length=150, unique=True)),
                ('keywords', models.CharField(blank=True, max_length=250)),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image')),
                ('preview_text', models.TextField(blank=True)),
                ('full_text', models.TextField(blank=True)),
                ('date_publish', models.DateTimeField(blank=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('tag_list', models.ManyToManyField(blank=True, related_name='post_list', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'db_table': 'blog_post',
                'ordering': ['-date_publish'],
            },
        ),
    ]