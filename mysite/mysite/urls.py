"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
import debug_toolbar
from app_news.sitemap import NewsSitemap


schema_view = get_schema_view(
    openapi.Info(
        title='Items API',
        default_version='v1',
        description='Описание проекта',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='admin@company.local'),
        license=openapi.License(name=''),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

sitemaps = {
    'news': NewsSitemap
}
urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('shopapp.urls')),
    path('req/', include('requestdataapp.urls')),
    path('users/', include('app_users.urls')),
    path('employment/', include('app_employment.urls')),
    path('news/', include('news_site.urls')),
    path('accounts/', include('myauth.urls')),
    path('files/', include('app_media.urls')),
    path('goods/', include('app_goods.urls')),
    path('blog/', include('blog_app.urls')),
    path('app_logic/', include('app_logic.urls')),
    path('app_pages/', include('app_pages.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/', include('new_app_users.urls')),
    path('api/', include('new_app_goods.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('market/', include('marketplace.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('blogs/', include('app_blogs.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('newss/', include('app_news.urls')),
    path('rss/', include('app_rss.urls')),
    path('', include('app_pages_new.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
