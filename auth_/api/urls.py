from django.urls import path
from . import views

urlpatterns = [
    path('comment-list', views.commentsList, name='api-comment-list'),
    path('comment-get/<str:pk>', views.commentGet, name='api-comment-detail'),
    path('comment-add', views.commentAdd, name='api-comment-add'),
    path('comment-edit/<str:pk>', views.commentEdit, name='api-comment-edit'),
    path('comment-delete/<str:pk>', views.commentDelete, name='api-comment-delete'),
]