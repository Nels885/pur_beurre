from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "app"
urlpatterns = [
    path('search/', views.search, name="search"),
    path('<int:product_id>/', views.food, name="food"),
    path('my_foods/', views.my_foods, name="my_foods"),
    path('account/', views.account, name="account"),
    path('registration/', views.registration, name="registration"),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
