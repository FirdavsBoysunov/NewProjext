from django.urls import path
from .views import RegisterView, VerifayEmailView, EmailVerifiedCheck

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("verify-email/", VerifayEmailView.as_view(), name="verify"),
    path("verify-email-check/", EmailVerifiedCheck.as_view(), name="verify-check"),


]