from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.index),
    path('resorts-single/',views.resort),
    path('resorts-grid',views.grid),
    path('about',views.about),
    path('travel-grid',views.travel_grid),
    path('travel-single/',views.travel_single),
    path('index',views.index),
    path('',views.index),
    path('contact',views.contact),
    path('search/',views.search),
    path('contact-form',views.contact_form),
    path("request-quote/",views.request_quote),
    path('hotels-regions/',views.hotels_regions),
    path('regions/<int:selected>',views.regions_list),
    path('quote',views.quote),
]
