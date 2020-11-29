from django.urls import path

from pets import views

urlpatterns = [
    path('', views.pet_all, name='pets'),
    path('details/<int:pk>', views.pet_detail, name='details'),
    path('like/<int:pk>', views.like, name='like'),
    path('create', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
