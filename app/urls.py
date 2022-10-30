from django.urls import path
from app import views

urlpatterns = [
    path('user/', views.user),
    path('userlist/', views.user_list),
    path('useradd/', views.user_add),
    path('useredit', views.user_edit)
]
