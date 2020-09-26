from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('stock/<symbol>/', views.stock_view, name='stock'),
    path('stock/', views.stock_view, name='stock'),
]