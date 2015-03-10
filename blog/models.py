from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.CharField(max_length=200)

class Blog(models.Model):
    subject = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.TimeField()
    blog_image = models.CharField(max_length=200)
    category = models.ForeignKey('Category')
 
class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_image = models.CharField(max_length=200)
    content  = models.TimeField()
    comment_time = models.TimeField()
    blog =  models.ForeignKey('Blog')