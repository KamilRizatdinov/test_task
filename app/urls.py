from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('query/', views.query, name='query'),
    path('all/', views.show_all, name='all'),
]
