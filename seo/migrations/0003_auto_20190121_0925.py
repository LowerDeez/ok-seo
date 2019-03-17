import django.core.validators
from django.db import migrations, models
import seo.utils


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_auto_20181126_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelinstanceseo',
            name='bottom_text',
        ),
        migrations.RemoveField(
            model_name='modelinstanceseo',
            name='top_text',
        ),
        migrations.RemoveField(
            model_name='viewseo',
            name='bottom_text',
        ),
        migrations.RemoveField(
            model_name='viewseo',
            name='top_text',
        ),
        migrations.AddField(
            model_name='modelinstanceseo',
            name='height',
            field=models.PositiveIntegerField(default=630, verbose_name='Image height'),
        ),
        migrations.AddField(
            model_name='modelinstanceseo',
            name='seo_text',
            field=models.TextField(blank=True, help_text='Can be useful for some static pages or some objects (like product category).', verbose_name='Seo text for page'),
        ),
        migrations.AddField(
            model_name='modelinstanceseo',
            name='width',
            field=models.PositiveIntegerField(default=1200, verbose_name='Image width'),
        ),
        migrations.AddField(
            model_name='viewseo',
            name='height',
            field=models.PositiveIntegerField(default=630, verbose_name='Image height'),
        ),
        migrations.AddField(
            model_name='viewseo',
            name='seo_text',
            field=models.TextField(blank=True, help_text='Can be useful for some static pages or some objects (like product category).', verbose_name='Seo text for page'),
        ),
        migrations.AddField(
            model_name='viewseo',
            name='width',
            field=models.PositiveIntegerField(default=1200, verbose_name='Image width'),
        ),
        migrations.AlterField(
            model_name='modelinstanceseo',
            name='follow',
            field=models.CharField(blank=True, choices=[('follow', 'Follow'), ('nofollow', 'No follow')], default='follow', max_length=15, verbose_name='Follow robots value'),
        ),
        migrations.AlterField(
            model_name='modelinstanceseo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=seo.utils.image_upload_to, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='modelinstanceseo',
            name='index',
            field=models.CharField(blank=True, choices=[('index', 'Index'), ('noindex', 'No index')], default='index', max_length=15, verbose_name='Index robots value'),
        ),
        migrations.AlterField(
            model_name='modelinstanceseo',
            name='object_type',
            field=models.CharField(blank=True, choices=[('article', 'Article'), ('website', 'Website')], default='article', max_length=40, verbose_name='Open graph type'),
        ),
        migrations.AlterField(
            model_name='modelinstanceseo',
            name='twitter_type',
            field=models.CharField(blank=True, choices=[('summary', 'Summary Card'), ('summary_large_image', 'Summary Card with Large Image'), ('player', 'Player'), ('app', 'App')], default='summary', max_length=40, verbose_name='Twitter type'),
        ),
        migrations.AlterField(
            model_name='viewseo',
            name='follow',
            field=models.CharField(blank=True, choices=[('follow', 'Follow'), ('nofollow', 'No follow')], default='follow', max_length=15, verbose_name='Follow robots value'),
        ),
        migrations.AlterField(
            model_name='viewseo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=seo.utils.image_upload_to, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='viewseo',
            name='index',
            field=models.CharField(blank=True, choices=[('index', 'Index'), ('noindex', 'No index')], default='index', max_length=15, verbose_name='Index robots value'),
        ),
        migrations.AlterField(
            model_name='viewseo',
            name='object_type',
            field=models.CharField(blank=True, choices=[('article', 'Article'), ('website', 'Website')], default='article', max_length=40, verbose_name='Open graph type'),
        ),
        migrations.AlterField(
            model_name='viewseo',
            name='twitter_type',
            field=models.CharField(blank=True, choices=[('summary', 'Summary Card'), ('summary_large_image', 'Summary Card with Large Image'), ('player', 'Player'), ('app', 'App')], default='summary', max_length=40, verbose_name='Twitter type'),
        ),
    ]
