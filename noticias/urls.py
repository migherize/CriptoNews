from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.main, name='main'),
    path('view_new/<str:noticia>/', views.view_new, name='view_new'),
    path('upload/', views.upload, name='upload'),
    path('filter/<str:filtro>/', views.filter, name='filter'),
    path('Insert/', views.insert_json, name='insert_json')
    ]