from django.db import models
from autoslug import AutoSlugField
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, related_name='author_blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # description = models.TextField()
    # description = RichTextField()
    description = RichTextUploadingField()
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    display_image = models.ImageField()
    slug = AutoSlugField(populate_from='title', unique=True)
    published_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    post_id = models.UUIDField(default=uuid.uuid4, unique=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, related_name='author_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(blank=False)
    published_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment

class SubComment(models.Model):
    author = models.ForeignKey(User, related_name='author_replies', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='sub_comments', on_delete=models.CASCADE)
    sub_comment = models.TextField(blank=False)
    published_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.sub_comment

    
