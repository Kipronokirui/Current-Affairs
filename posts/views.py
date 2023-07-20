from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import (Category, CategorySerializer, Post, 
                          PostSerializer, CreateCategorySerializer,
                          CreatePostSerializer, CreateCommentSerializer, Comment,
                          CreateSubCommentSerializer, SubComment
                          )

class CategoryListView(APIView):
    # queryset=Category.objects.all()
    # serializer_class=CategorySerializer
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

class CreateCategoryView(APIView):
    def post(self, request):
        serializer = CreateCategorySerializer(data = request.data, partial=True)
        print(f'Serializers is {serializer}')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreatePostView(APIView):
    def post(self, request):
        serializer = CreatePostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListView(APIView):
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
        def post(self, request, slug=None):
            data = request.data
            post = Post.objects.get(slug=slug)
            comment=Comment.objects.create(
                post=post,
                comment=data['comment']
            )
            return Response("Comment Added")
        
class CreateCommentReplyView(APIView):
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