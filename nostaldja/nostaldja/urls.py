from django.urls import path
from . import views

urlpatterns = [
    path('decades', views.decades_list, name='decades_list'),
    path('fads', views.fads_list, name='fads_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('decades/<int:pk>/edit', views.decade_edit, name='decade_edit'),
    path('decades/<int:pk>/delete', views.decade_delete, name='decade_delete'),
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete')
]
