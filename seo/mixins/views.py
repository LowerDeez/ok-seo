from typing import Dict

from ..models.instance_based import ModelInstanceSeo
from ..models.view_based import ViewSeo
from ..models.url_based import UrlSeo
from ..utils import get_path_from_request

__all__ = (
    'UrlSeoMixin',
    'ViewSeoMixin',
    'ModelInstanceViewSeoMixin'
)


class UrlSeoMixin:
    """
    Mixin to add meta tags from UrlSeo, found by a current path
    """

    def get_seo(self) -> Dict[str, ViewSeo]:
        path = get_path_from_request(request=self.request)
        return {
            'seo': (
                UrlSeo
                .objects
                .filter(url=path)
                .first()
            )
        }

    def get_context_data(self, **kwargs) -> Dict:
        kwargs.update(self.get_seo())
        return super().get_context_data(**kwargs)


class ViewSeoMixin(UrlSeoMixin):
    """
    Mixin to add meta tags from ViewSeo, found by a given template
    """
    seo_view = ''  # type: str

    def get_seo(self) -> Dict[str, ViewSeo]:
        return {
            'seo': (
                ViewSeo
                .objects
                .filter(view=self.seo_view)
                .first()
            )
        }


class ModelInstanceViewSeoMixin(ViewSeoMixin):
    """
    Mixin to add meta tags from ModelInstanceSeo, found by a current content object
    """
    def get_seo(self):
        return {
            'seo': (
                ModelInstanceSeo
                .objects
                .filter_by_instance(self.object)
                .first()
            )
        }
