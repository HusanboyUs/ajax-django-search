from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('search/',views.search_results, name='search'),
    path('<int:pk>/', views.game_detail_view, name='detail_view'),
]
