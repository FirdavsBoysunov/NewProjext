from django.urls import path
from .views import RegisterView, VerifayEmailView, EmailVerifiedCheck, LoginView, HomeView, LogoutView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetCompleteView, PasswordResetDoneView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("verify-email/", VerifayEmailView.as_view(), name="verify"),
    path("verify-email-check/", EmailVerifiedCheck.as_view(), name="verify-check"),
    path("home/", HomeView.as_view(),name='home')

]