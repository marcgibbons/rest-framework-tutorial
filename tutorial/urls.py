from snippets import views
from django.conf.urls import patterns, url, include

from coreapi_swagger.contrib.django.renderers import SwaggerRenderer
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.routers import DefaultRouter

# TODO: this is a quick hack for demo
# would want to allow schema_renderers to be set from the init.
class SwaggerRouter(DefaultRouter):
    schema_renderers = [CoreJSONRenderer, SwaggerRenderer]


router = SwaggerRouter(schema_title='Pastebin API')
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
