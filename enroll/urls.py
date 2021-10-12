from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.savedata, name='save'),
    path('delete/', views.delete_data, name='delete'),
    path('edit/', views.edit_data, name="edit")
]