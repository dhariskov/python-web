from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile edit'),
    path('profile/delete', views.profile_delete, name='profile delete'),
]