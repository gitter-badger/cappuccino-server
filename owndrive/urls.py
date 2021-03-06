
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from owndrive import settings
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^', include('owndrive.apps.client.urls')),
    url(r'^', include('owndrive.apps.command.urls')),
    url(r'^', include('owndrive.apps.upload.urls')),
    url(r'^', include('owndrive.apps.download.urls')),
    url(r'^', include('owndrive.apps.login.urls')),

    # Comment the following line to disable the admin
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
