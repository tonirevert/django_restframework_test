from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from blog.models import Post, Comment, UserProfile
from .serializers import PostSerializer, CommentSerializer, UserProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @detail_route(methods=['post'])
    def set_comment(self, request, pk=None):

        my_post = self.get_object()

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=my_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)