"""
URL configuration for secure_app.
"""

from django.urls import path

from secure_app import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path(
        'account-locked/',
        views.AccountLockedView.as_view(),
        name='account_locked'
    ),
]
