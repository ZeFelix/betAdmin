from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from betAdmin.accounts import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('signup/', account_views.register, name='signup'),

    path('logout', auth_views.LogoutView.as_view(),name='logout'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='passowrd_reset.html',
             email_template_name='password_reset_email.html',
             success_url=reverse_lazy('accounts:password_reset_done')
         ),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html',
             success_url=reverse_lazy('accounts:login')
         ),
         name='password_reset_confirm'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account_views.activate, name='activate'),
]
