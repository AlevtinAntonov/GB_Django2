from django.urls import path

from . import views

app_name = 'myapp6'
urlpatterns = [
    path('', views.index, name='index'),
]