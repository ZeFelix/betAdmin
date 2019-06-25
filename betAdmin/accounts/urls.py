from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', auth_views.LoginView.as_view(template_name='signup.html'), name='signup')
]
