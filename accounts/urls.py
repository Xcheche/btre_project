from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# Define the app name for namespacing the URLs
app_name = "accounts"

# Define the URL patterns for the accounts app
urlpatterns = [
    # URL pattern for the register view
    path("register/", views.register, name="register"),
    # URL pattern for the login view
    path("login/", views.login, name="login"),
    # URL pattern for the logout view
    path("logout/", views.logout, name="logout"),
    # URL pattern for the dashboard view
    path("dashboard/", views.dashboard, name="dashboard"),
    
        #Password reset
      path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html'
         ),
         name='password_reset'),#1
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),#2
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),#3
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
