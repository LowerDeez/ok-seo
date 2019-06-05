from ..settings import SEO_USE_URL_SEO

from .filters import *
from .inline import *
from .utils import *

if SEO_USE_URL_SEO:
    from .url_seo import *
else:
    from .url_seo import *
    from .model_instance_seo import *
    from .view_seo import *
