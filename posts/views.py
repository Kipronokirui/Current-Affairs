from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import (Category, CategorySerializer, Post, 
                          PostSerializer, CreateCategorySerializer,
                          CreatePostSerializer, CreateCommentSerializer, Comment,
                          CreateSubCommentSerializer, SubComment
                          )
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class CategoryListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
    def get(self, request, id=None):
        if id is None:
            categorys = Category.objects.all()
            serializer = CategorySerializer(categorys, context={"request": request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, id=None):
        if id is not None:
            category = Category.objects.get(id=id)
            serializer = CreateCategorySerializer(category, data = request.data, partial=True)
            print(f'Serializers is {serializer}')
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryUpdateView(APIView):
    permission_classes = [IsAdminUser]
    def put(self, request, id=None):
        if id is not None:
            category = Category.objects.get(id=id)
            serializer = CreateCategorySerializer(category, data = request.data, partial=True)
            print(f'Serializers is {serializer}')
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCategoryView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = CreateCategorySerializer(data = request.data, partial=True)
        # print(f'Serializers is {serializer}')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        user = request.user.id
        data['author'] = user
        serializer = CreatePostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, slug=None):
        if slug is None:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, context={"request": request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        post = Post.objects.get(slug=slug)
        serializer = PostSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug=None):
        if slug is not None:
            post = Post.objects.get(slug=slug)
            serializer = CreatePostSerializer(post, data = request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCommentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, slug=None):
        data = request.data
        user = request.user
        post = Post.objects.get(slug=slug)
        comment=Comment.objects.create(
            author = user,
            post=post,
            comment=data['comment']
        )
        return Response("Comment Added")
        
class CreateCommentReplyView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id=None):
        data = request.data
        comment = Comment.objects.get(id=id)
        reply=SubComment.objects.create(
            comment=comment,
            sub_comment=data['sub_comment']
        )
        data = {}
        if reply:
            data["success"] = "Reply was successful added"
        else:
            data["failure"] = 'An error occured'
        return Response(data=data)