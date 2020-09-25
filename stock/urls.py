from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<symbol>/', views.stock_view, name='stock'),
]