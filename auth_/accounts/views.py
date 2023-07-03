from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateUserForm
from comments.models import Comments
from django.shortcuts import get_object_or_404


def home(request):
    comments = Comments.objects.all()
    #post = get_object_or_404(Comments, id=request.POST.get('comment_like_id'))
    return render(request, 'home.html', {'comments': comments})

class SignUpView(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
