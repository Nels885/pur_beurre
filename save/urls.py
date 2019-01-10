from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "save"
urlpatterns = [
    path('my_foods/', views.my_foods, name="my_foods"),
    path('<str:search_prod>/<int:subs_id>/', views.backup, name="backup"),
]
