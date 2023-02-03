
# Create your models here.
# Category
# Tag
# Post

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
#Third party apps
from autoslug import AutoSlugField
from tinymce.models import HTMLField


# Create your models here.
class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:category_view', # category_view must be unique bcz of that we wrote namespace 
            kwargs={
                "category_slug": self.slug,
            }
        )

class BlogTag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog:tag_view',
            kwargs={
                "tag_slug": self.slug,
            }
        )

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    tag=models.ManyToManyField(BlogTag)
    cover_image = models.ImageField(upload_to ='post/')    
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', 
    unique=True, 
    #blank=True,
    )
    content = HTMLField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    view_count = models.PositiveBigIntegerField(default=0)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    # TODO get_absolute_url    
    # def get_absolute_url(self):
    #     return reverse(
    #         'todo:todo_detail_view',
    #         kwargs={
    #             "category_slug": self.category.slug,
    #             "id":self.pk,
    #         }
    #     )  