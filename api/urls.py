from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('subjects', views.subjects_list, name='subjects'),
]
