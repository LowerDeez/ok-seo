from django.test import TestCase
from django.test.client import RequestFactory
from django.template import Context, Template

from ..models.view_based import ViewSeo

__all__ = (
    'GetSeoDataTemplateTagTest',
)


class GetSeoDataTemplateTagTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rendered(self):
        seo = ViewSeo(
            title='1',
            description='1',
            keywords='1,2,3',
            object_type='article'
        )
        request = self.factory.get('/')
        context = Context({'seo': seo, 'debug': True})
        context.request = request
        context.debug = True
        template_to_render = Template(
            '{% load seo %}'
            '{% get_seo_data seo %}'
        )
        rendered_template = template_to_render.render(context)
        self.assertInHTML(
            f'<title>{seo.get_meta_title()}</title>',
            rendered_template
        )
        self.assertInHTML(
            f'<meta name="description" content="{seo.get_meta_description()}">',
            rendered_template
        )
        self.assertInHTML(
            f'<meta name="keywords" content="{seo.get_meta_keywords()}">',
            rendered_template
        )
        self.assertInHTML(
            f'<meta property="og:type" content="{seo.get_opengraph_type()}">',
            rendered_template
        )
        self.assertInHTML(
            f'<meta property="og:title" content="{seo.get_meta_title()}">',
            rendered_template
        )
        self.assertInHTML(
            f'<meta property="og:description" content="{seo.get_meta_description()}">',
            rendered_template
        )
        self.assertInHTML(
            f'<meta name="twitter:card" content="{seo.get_twitter_type()}">',
            rendered_template
        )
