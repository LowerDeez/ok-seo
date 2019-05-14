# Generated by Django 2.1.4 on 2019-05-14 09:28

import django.core.validators
from django.db import migrations, models
import seo.mixins.models
import seo.utils


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0005_auto_20190323_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(blank=True, choices=[('article', 'Article'), ('website', 'Website')], default='article', max_length=40, verbose_name='Open graph type')),
                ('twitter_type', models.CharField(blank=True, choices=[('summary', 'Summary Card'), ('summary_large_image', 'Summary Card with Large Image'), ('player', 'Player'), ('app', 'App')], default='summary', max_length=40, verbose_name='Twitter type')),
                ('index', models.CharField(blank=True, choices=[('index', 'Index'), ('noindex', 'No index')], default='index', max_length=15, verbose_name='Index robots value')),
                ('follow', models.CharField(blank=True, choices=[('follow', 'Follow'), ('nofollow', 'No follow')], default='follow', max_length=15, verbose_name='Follow robots value')),
                ('canonical', models.CharField(blank=True, max_length=255, verbose_name='Canonical')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Seo Title')),
                ('keywords', models.TextField(blank=True, verbose_name='Meta Keywords')),
                ('description', models.TextField(blank=True, verbose_name='Meta Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=seo.utils.image_upload_to, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])], verbose_name='Image')),
                ('width', models.PositiveIntegerField(default=1200, verbose_name='Image width')),
                ('height', models.PositiveIntegerField(default=630, verbose_name='Image height')),
                ('alt', models.CharField(blank=True, max_length=255, verbose_name='Image alt text')),
                ('h1', models.CharField(blank=True, max_length=255, verbose_name='H1 title')),
                ('seo_text', models.TextField(blank=True, help_text='Can be useful for some static pages or some objects (like product category).', verbose_name='Seo text')),
                ('url', models.CharField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Url seo',
                'verbose_name_plural': 'Url seo',
            },
            bases=(seo.mixins.models.SeoTagsMixin, models.Model),
        ),
    ]
