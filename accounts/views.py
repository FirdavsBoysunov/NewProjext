from django.shortcuts import render
from .forms import *
from django.views.generic import CreateView, View
from .models import CustomUser
from django.core.signing import Signer
from django.urls import reverse
from utils.functions import send_verification_email
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
        try:

            CustomUser.objects.get(id = user_id)
            return render(request, 'user/email-verified.html', {"verified": True})
        except:
            return render(request, 'user/email-verified.html', {"verified": False})

