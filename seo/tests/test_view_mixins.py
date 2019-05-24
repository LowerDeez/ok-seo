from django.contrib.auth.models import User
from django.test import TestCase

from ..mixins.views import ViewSeoMixin, ModelInstanceViewSeoMixin
from ..models.view_based import ViewSeo
from ..models.instance_based import ModelInstanceSeo

__all__ = (
    'ViewSeoMixinTestCase',
)


class TestViewSeoMixin(ViewSeoMixin):
    seo_view = 'test'


class ViewSeoMixinTestCase(TestCase):
    def setUp(self) -> None:
        self.seo = ViewSeo.objects.create(view='test')

    def test_view_seo_mixin(self):
        seo = TestViewSeoMixin().get_seo()
        self.assertEqual(self.seo, seo['seo'])


class ModelInstanceViewSeoMixinTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user('username')
        self.seo = ModelInstanceSeo.objects.create(content_object=self.user)

    def test_model_instance_view_seo_mixin(self):
        class TestModelInstanceViewSeoMixin(ModelInstanceViewSeoMixin):
            object = self.user
        seo = TestModelInstanceViewSeoMixin().get_seo()
        self.assertEqual(self.seo, seo['seo'])