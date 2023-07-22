from django.urls import path
from .views import (CategoryListView, PostListView, CreateCategoryView, 
                    CreatePostView, CreateCommentView, CreateCommentReplyView,
                    CategoryUpdateView)

urlpatterns = [
    path('categorys/', CategoryListView.as_view()),
    path('category/<str:id>/', CategoryListView.as_view()),
    path('category/<str:id>/update/', CategoryListView.as_view()),
    path('create/category/', CreateCategoryView.as_view()),
    path('posts/', PostListView.as_view()),
    path('post/create/', CreatePostView.as_view()),
    path('posts/<str:slug>/', PostListView.as_view()),
    path('posts/<str:slug>/add-comment/', CreateCommentView.as_view()),
    path('comment/<str:id>/add-reply/', CreateCommentReplyView.as_view()),
]
    