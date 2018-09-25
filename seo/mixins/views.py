from typing import Dict

from ..models.instance_based import ModelInstanceSeo
from ..models.view_based import ViewSeo

__all__ = (
    'ViewSeoMixin',
    'ModelInstanceViewSeoMixin'
)


class ViewSeoMixin:
    """
    Mixin to add meta tags from ViewSeo found by given template
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

    def get_context_data(self, **kwargs) -> Dict:
        kwargs.update(self.get_seo())
        return super().get_context_data(**kwargs)


class ModelInstanceViewSeoMixin(ViewSeoMixin):
    """
    Mixin to fetch seo data for current object
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
