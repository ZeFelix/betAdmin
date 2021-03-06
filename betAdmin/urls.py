from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
    path('', include('betAdmin.core.urls', namespace='core')),
    path('accounts/', include('betAdmin.accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
]
