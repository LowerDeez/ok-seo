from django.test import TestCase,override_settings
from django.test.client import RequestFactory
from django.template import Context, Template
from django.contrib.flatpages.models import FlatPage

from ..models.instance_based import ModelInstanceSeo

__all__ = (
    'GetSeoDataTemplateTagTestFromInstanceModel',
)

@override_settings(SEO_MODELS=["flatpages.FlatPage"])
class GetSeoDataTemplateTagTestFromInstanceModel(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_modelinstanceseo_rendered(self):
        flatpage = FlatPage.objects.create(
                title="title",
                url="index/",
                content="content")
        seo = ModelInstanceSeo(
            title='1',
            description='1',
            keywords='1,2,3',
            object_type='article',
            content_object=flatpage,
        )
        seo.save()
        request = self.factory.get('/pages/index/')
        context = Context({'flatpage': flatpage,
            'debug': True})
        context.request = request
        context.debug = True
        template_to_render = Template(
            '{% load seo %}'
            '{% get_seo_data flatpage %}'
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            f'<title>{seo.get_meta_title()}</title>',
            rendered_template
        )

