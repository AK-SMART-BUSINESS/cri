from django.urls import path

from . import views

app_name = 'mainsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('apropos', views.about, name='about')
]