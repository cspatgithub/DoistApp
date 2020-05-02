from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('doist-admin-console/', admin.site.urls),
    path('', include('apps.tasks.urls')),
    path('', include('apps.notes.urls')),
    path('accounts/', include('apps.accounts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
