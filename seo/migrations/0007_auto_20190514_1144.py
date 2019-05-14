# Generated by Django 2.1.4 on 2019-05-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0006_urlseo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlseo',
            name='url',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Url'),
        ),
    ]