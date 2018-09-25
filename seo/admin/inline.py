from .utils import get_admin_inline_base_class
from ..models.instance_based import ModelInstanceSeo

__all__ = (
    'ModelInstanceSeoInline',
)


class ModelInstanceSeoInline(get_admin_inline_base_class()):
    classes = ['collapse']
    extra = 1
    model = ModelInstanceSeo
    max_num = 1
