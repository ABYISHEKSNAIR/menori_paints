from django import views
from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.index,name='HOME'),
    path('about/', views.about,name='ABOUT'),
     path('products/', views.products,name='PRODUCTS'),
     path('interior/', views.interior,name='INTERIOR'),
     path('primer/', views.primer,name='PRIMER'),
     path('exterior/', views.exterior,name='EXTERIOR'),
      path('dealers/', views.dealers,name='DEALERS'),
       path('careers', views.careers,name='CAREERS'),
        path('contact', views.contact,name='CONTACT'),
]
