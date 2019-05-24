from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url
from django.contrib import admin

urlpatterns = i18n_patterns(
    url(r"^admin/", admin.site.urls),
)
