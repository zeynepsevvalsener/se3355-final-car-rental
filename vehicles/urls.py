from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# Django'nun i18n rotaları
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
      path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Google OAuth vb.
]

# Uygulama rotaları ve i18n
urlpatterns += i18n_patterns(
    path('', include('MyApp.urls')),
)

# Static/Media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
