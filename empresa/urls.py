from django import urls
from django.contrib import admin
from django.urls import re_path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from register.views import UserViewSet, ClientViewSet, CompanyViewSet, ManagerViewSet
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Desafio Hora da Pratica 02",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='User')
router.register(r'client', ClientViewSet, basename='Client')
router.register(r'company', CompanyViewSet, basename='Company')
router.register(r'manager', ManagerViewSet, basename='Manager')
# router.register('document', DocsViewSet, basename='Document')


urlpatterns = [
    re_path(r'^v1/admin/', admin.site.urls),
    re_path(r'^v1/api-auth/', include('rest_framework.urls', namespace='v1')),
    re_path(r'^v1/', include(router.urls)),
    re_path(r'^v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


STATIC_ROOT = "/var/www/example.com/static/"



