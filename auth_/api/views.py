from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CommentsSerializer
from comments.models import Comments

# Create your views here.
@api_view(['GET'])
def commentsList(request):
    comments = Comments.objects.all()
    serializer = CommentsSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def commentGet(request, pk):
    comment = Comments.objects.get(id=pk)
    serializer = CommentsSerializer(comment, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def commentAdd(request):
    serializer = CommentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST', 'GET'])
def commentEdit(request, pk):
    comment = Comments.objects.get(id=pk)
    serializer = CommentsSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def commentDelete(request, pk):
    comment = Comments.objects.get(id=pk)

    comment.delete()

    return Response("item deleted")


