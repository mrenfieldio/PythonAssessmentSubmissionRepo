
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_repositories, name='search_repositories'),
    path('error/', views.error, name='error'),
]
