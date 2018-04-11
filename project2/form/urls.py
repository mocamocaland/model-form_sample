from django.urls import path
from .import views

app_name = 'form'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('category/', views.CategoryCreateView.as_view(), name='category'),
]