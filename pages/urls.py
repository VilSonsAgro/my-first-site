from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.HomePageView.as_view(), name='home'),
    path('about_us/', views.AboutPageView.as_view(), name='about_us'),
    path('products/', views.ProductsPageView.as_view(), name='products'),
    path('food_safety/', views.FoodSafetyPageView.as_view(), name='food_safety'),
    path('contact_us/', views.ContactUsPageView.as_view(), name='contact_us'),
    path('feedback/', views.FeedBackPageView.as_view(), name='feedback'),
    path('feedback/<int:pk>', views.HomeView, name='contact_us'),
]
