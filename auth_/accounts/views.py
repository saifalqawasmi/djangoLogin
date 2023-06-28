from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateUserForm
from comments.models import Comments


def home(request):
    comments = Comments.objects.all()
    return render(request, 'home.html', {'comments': comments})

class SignUpView(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
