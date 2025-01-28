"""
URL configuration for secure_app.
"""

from django.urls import path

from secure_app import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
]
