from django.urls import path
from django.contrib.auth import views as auth_views
from betAdmin.accounts import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', account_views.register, name='signup')
]
