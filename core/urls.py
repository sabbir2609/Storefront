from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('store/', include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("api-auth/", include("rest_framework.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

handler404 = 'home.views.handler404'
