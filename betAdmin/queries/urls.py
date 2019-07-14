from django.urls import path
from betAdmin.queries import views

app_name = 'queries'

urlpatterns = [
    path('statement/', views.index, name='queries')
]