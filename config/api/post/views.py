from re import L, search
from django.db.models import query
from django.shortcuts import render
from rest_framework import pagination, serializers


from .models import Post
from .serialize import PostSerialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,authentication, permissions

from rest_framework.generics import ListAPIView,ListCreateAPIView
# from .pagination import CustomPagination
# from config.api.pagination import CustomPagination
from ..pagination import CustomPagination
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialize
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['title','category']

    def perform_create(self, serializer):
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostTable(ListAPIView):
    def get(self,request):        
        posts = Post.objects.all()
        postSerialize = PostSerialize(posts,many=True)
        # pagination_class = PageNumberPagination
        # return Response(postSerialize.data)    
    def post(self,request):
        post = PostSerialize(data=request.data)
        if (post.is_valid()):
            post.save()
            return Response(post.data,status=status.HTTP_201_CREATED)
        return Response(post.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
  
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerialize(post)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerialize(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        if(post):
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error":"id not valid"}, status=status.HTTP_400_BAD_REQUEST)