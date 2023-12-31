from rest_framework import serializers
from .models import SubComment, Comment, Post, Category 

class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = '__all__'

class CreateSubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = ['comment', 'sub_comment']
        
class CommentSerializer(serializers.ModelSerializer):
    sub_comments = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'published_at', 'edited_at', 'post', 'author', 'sub_comments']
        
    def get_sub_comments(self, obj):
        sub_comments = obj.sub_comments.all()
        serializer = SubCommentSerializer(sub_comments, many=True)
        return serializer.data
    
class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'post']      

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'display_image', 'image_url', 'slug', 'published_at', 'edited_at', 'post_id', 'comments']
        
    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data
    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.display_image.url)

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'display_image', 'category', 'author']

class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'posts']
        
    def get_posts(self, obj):
        posts = obj.posts.all()
        serializer = PostSerializer(posts, many=True)
        return serializer.data

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description']