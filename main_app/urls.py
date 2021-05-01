from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_page, name='index'),
    path('hotels/', views.hotels_page, name='hotels'),
    path('help/', views.help_page, name='help'),
    path('privacy/', views.privacy_page, name='privacy'),
]
