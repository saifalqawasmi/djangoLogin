from django.urls import path

from . import views

urlpatterns = [
    path('add', views.addComment, name='comment-add'),
    path('edit/<int:id>', views.editComment, name='comment-edit'),
]