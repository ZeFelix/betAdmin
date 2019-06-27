from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from betAdmin.accounts import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', account_views.register, name='signup'),
    path('recovery-password/', account_views.recovery_password, name='recovery-password'),
    #path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', account_views.activate, name='activate'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',account_views.activate , name='activate'),
]