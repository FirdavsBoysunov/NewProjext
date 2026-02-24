from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import CreateView, View, TemplateView
from .models import CustomUser
from django.core.signing import Signer
from django.urls import reverse
from utils.functions import send_verification_email
from django.contrib.auth import authenticate, login, logout

signer = Signer()

class RegisterView(CreateView):
    form_class = RegisterForm
    model = CustomUser
    template_name = 'user/register.html'
    
    def get_success_url(self):
        return reverse("verify-check")

    def form_valid(self, form):

        user_id = form.instance.id
        token = signer.sign(str(user_id))
        send_verification_email(form.instance.email, token)

        return super().form_valid(form)

class EmailVerifiedCheck(View):
    
    def get(self, request):

        return render(request, 'user/verify.html')


class VerifayEmailView(View):

    def get(self, request):
        token = request.GET.get("token")
        user_id = signer.unsign(token)
        context = {"verifed":False}
        try:

            user = CustomUser.objects.get(id = user_id)
            user.verify_email
            context["verifed"] = True
        except:
            pass
            return render(request, 'user/email-verified.html',context)

class LoginView(View):

    def get(self, request):
        return render(request, 'user/login.html')
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,**form.cleaned_data)
            if not user or not user.email_verified:
                return render(request, 'user/login.html',{"error":"user not found or not verified"})
            login(request,user)
            return redirect("home")    
        return render(request, 'user/login.html',{"error":"enter valid data"})


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {'message':'leyohouu!'}
        return context
    


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("login")