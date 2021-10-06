from django import urls
from django.contrib import admin
from django.urls import path
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
router.register('user', UserViewSet, basename='User')
router.register('client', ClientViewSet, basename='Client')
router.register('company', CompanyViewSet, basename='Company')
router.register('manager', ManagerViewSet, basename='Manager')
# router.register('document', DocsViewSet, basename='Document')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

STATIC_ROOT = "/var/www/example.com/static/"



