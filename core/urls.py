from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_pk>/close/', views.close, name='close'),
    path('<int:task_pk>/open/', views.open, name='open'),
]
