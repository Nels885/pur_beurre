from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "app"
urlpatterns = [
    path('results/', views.results, name="results"),
    path('food/', views.food, name="food"),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name="login"),
    path('logout/', views.logout, name="logout"),
]
