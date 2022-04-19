from django.contrib import admin
from django.urls import path,include
from .documentation_schema import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
