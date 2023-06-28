from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateUserForm


def home(request):
    return render(request, 'home.html')

class SignUpView(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
