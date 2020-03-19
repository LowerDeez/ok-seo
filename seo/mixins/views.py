from typing import Dict

from ..models.instance_based import ModelInstanceSeo
from ..models.view_based import ViewSeo
from ..models.url_based import UrlSeo
from ..services import get_url_seo
from ..settings import SEO_VIEWS_CONTEXT_NAME

__all__ = (
    'UrlSeoMixin',
    'ViewSeoMixin',
    'ModelInstanceViewSeoMixin'
)


class UrlSeoMixin:
    """
    Mixin to add meta tags from UrlSeo, found by a current path
    """

    def get_seo(self) -> Dict[str, UrlSeo]:
        seo = get_url_seo(request=self.request)
        return {
            SEO_VIEWS_CONTEXT_NAME: seo
        }

    def get_context_data(self, **kwargs) -> Dict:
        kwargs.update(self.get_seo())
        return super().get_context_data(**kwargs)


class ViewSeoMixin(UrlSeoMixin):
    """
    Mixin to add meta tags from ViewSeo,
    found by a given template
    """
    seo_view = ''  # type: str

    def get_seo(self) -> Dict[str, ViewSeo]:
        return {
            SEO_VIEWS_CONTEXT_NAME: (
                ViewSeo
                .objects
                .filter(
                    view=self.seo_view
                )
                .first()
            )
        }


class ModelInstanceViewSeoMixin(ViewSeoMixin):
    """
    Mixin to add meta tags from ModelInstanceSeo,
    found by a current content object
    """
    def get_seo(self):
        return {
            SEO_VIEWS_CONTEXT_NAME: (
                ModelInstanceSeo
                .objects
                .filter_by_instance(self.object)
                .first()
            )
        }
