from django.urls import path

from . import views

urlpatterns = [
    path('results/', views.results, name="results"),
    path('food/', views.food, name="food"),
    path('account/', views.account, name="account"),
]
