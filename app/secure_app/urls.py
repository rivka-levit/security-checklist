"""
URL configuration for secure_app.
"""

from django.urls import path
from django.contrib.auth import views as auth_views

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

    # Password management

    # Enter an email for password reset link
    path(
        'reset-password/',
        auth_views.PasswordResetView.as_view(
            template_name='secure_app/password/password_reset.html'
        ),
        name='reset_password'
    ),

    # Success page that the email has been sent to reset password
    path(
        'reset-password/sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='secure_app/password/password_reset_sent.html'
        ),
        name='password_reset_done'
    ),

    # Send a link to reset password. Presents a form for entering a new password
    path(
        'reset-password-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='secure_app/password/password_reset_form.html'
        ),
        name='password_reset_confirm'
    ),

    # Success page password has been changed successfully
    path(
        'reset-password-complete',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='secure_app/password/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
