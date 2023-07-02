from django.urls import path

from . import views

urlpatterns = [
    path('add', views.addComment, name='comment-add'),
    # path('edit/<str:id>', views.EditCommentView.as_view(), name='comment-edit'),
]