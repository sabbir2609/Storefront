from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('_debug_/', include(debug_toolbar.urls)),
]
