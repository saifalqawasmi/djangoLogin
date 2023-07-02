from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Comments

# Create your views here.


def addComment(request):
    comments = Comments.objects.all()
    return render(request, 'commentA.html', {'comments': comments})