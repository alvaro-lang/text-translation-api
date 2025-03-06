from django.urls import path, include
from django.contrib import admin

api_urls = [
    path('auth/', include("apps.custom_auth.urls")),
    path('translation/', include("apps.translation.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
