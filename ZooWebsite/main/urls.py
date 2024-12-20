from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('prices/', views.prices, name='prices'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),

    path('reviews/', views.reviews, name='reviews'),
    path('reviews/add/', views.add_review, name='add_review'),
]
