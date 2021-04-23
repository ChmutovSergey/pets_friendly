from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_page, name='index'),
    path('hotels/', views.hotels_page, name='hotels'),
    # path('hotels/<int:hotel_id>/', views.card_hotel_page, name='card_hotel'),
    path('help/', views.help_page, name='help'),
]
