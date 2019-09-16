from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('', include('betAdmin.core.urls', namespace='core')),
    path('payments/', include('betAdmin.payments.urls', namespace='payments')),
    path('accounts/', include('betAdmin.accounts.urls', namespace='accounts')),
    path('queries/', include('betAdmin.queries.urls', namespace='queries')),
    path('admin/', admin.site.urls),

    path('api/v1/', include('betAdmin.accounts.api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
