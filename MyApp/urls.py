from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),

    path('vehicles/', views.vehicles, name='vehicles'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('bill/', views.bill, name='bill'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),

    path('search/', views.search, name='search'),
    path('nearest-offices/', views.nearest_offices, name='nearest_offices'),
]
