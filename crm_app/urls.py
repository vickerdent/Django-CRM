from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('record/<str:pk>', views.customer_record, name="record"),
    path('delete/<str:pk>', views.delete_record, name="delete"),
    path('add_record/', views.add_record, name="add_record"),
    path('edit_record/<str:pk>', views.edit_record, name="edit_record"),
]