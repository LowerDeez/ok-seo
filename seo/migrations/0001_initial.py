import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import seo.mixins.models
import seo.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelInstanceSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_app_id', models.CharField(blank=True, max_length=40, verbose_name='Facebook app id')),
                ('object_type', models.CharField(blank=True, choices=[('website', 'Website'), ('article', 'Article')], max_length=40, verbose_name='Open graph type')),
                ('twitter_type', models.CharField(blank=True, choices=[('summary', 'Summary Card'), ('summary_large_image', 'Summary Card with Large Image'), ('player', 'Player'), ('app', 'App')], max_length=40, verbose_name='Twitter type')),
                ('index', models.CharField(blank=True, choices=[('index', 'Index'), ('noindex', 'No index')], max_length=15, verbose_name='Index robots value')),
                ('follow', models.CharField(blank=True, choices=[('follow', 'Follow'), ('nofollow', 'No follow')], max_length=15, verbose_name='Follow robots value')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Seo Title')),
                ('keywords', models.TextField(blank=True, verbose_name='Meta Keywords')),
                ('description', models.TextField(blank=True, verbose_name='Meta Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=seo.utils.image_upload_to, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])], verbose_name='Изображение')),
                ('alt', models.CharField(blank=True, max_length=255, verbose_name='Alt')),
                ('object_id', models.CharField(help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Object Primary Key')),
                ('content_type', models.ForeignKey(help_text='Please select the type (model) for the relation, you want to build.', limit_choices_to={'model__in': ['article']}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Content Type')),
            ],
            options={
                'verbose_name': 'Model instance seo',
                'verbose_name_plural': 'Model instance seo',
            },
            bases=(seo.mixins.models.SeoTagsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ViewSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_app_id', models.CharField(blank=True, max_length=40, verbose_name='Facebook app id')),
                ('object_type', models.CharField(blank=True, choices=[('website', 'Website'), ('article', 'Article')], max_length=40, verbose_name='Open graph type')),
                ('twitter_type', models.CharField(blank=True, choices=[('summary', 'Summary Card'), ('summary_large_image', 'Summary Card with Large Image'), ('player', 'Player'), ('app', 'App')], max_length=40, verbose_name='Twitter type')),
                ('index', models.CharField(blank=True, choices=[('index', 'Index'), ('noindex', 'No index')], max_length=15, verbose_name='Index robots value')),
                ('follow', models.CharField(blank=True, choices=[('follow', 'Follow'), ('nofollow', 'No follow')], max_length=15, verbose_name='Follow robots value')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Seo Title')),
                ('keywords', models.TextField(blank=True, verbose_name='Meta Keywords')),
                ('description', models.TextField(blank=True, verbose_name='Meta Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=seo.utils.image_upload_to, validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])], verbose_name='Изображение')),
                ('alt', models.CharField(blank=True, max_length=255, verbose_name='Alt')),
                ('view', models.CharField(choices=[('index', 'Index')], max_length=100, unique=True, verbose_name='View')),
            ],
            options={
                'verbose_name': 'View seo',
                'verbose_name_plural': 'View seo',
            },
            bases=(seo.mixins.models.SeoTagsMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='modelinstanceseo',
            unique_together={('content_type', 'object_id')},
        ),
    ]
