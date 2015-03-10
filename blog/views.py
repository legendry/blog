#encoding=utf8
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Category, Blog, Comment
        
def _todetail(request,blogid):
    myblog = Blog.objects.get(id=blogid)
    return render(request,'blog/detail.html',{"blog":myblog})
      
def detail(request,blogid):
    return _todetail(request,blogid)

def addcommnent(reqeust):
    user_name = reqeust.POST["username"]
    user_email = reqeust.POST["email"]
    user_image = reqeust.POST["image"]
    blogid = reqeust.POST["blogid"]
    content = reqeust.POST["comment"]
    myblog = Blog.objects.get(id=blogid)
    mycomment = Comment.objects.create()
    mycomment.user_name = user_name
    mycomment.user_email = user_email
    mycomment.user_img = user_image
    mycomment.blog_id = myblog
    mycomment.content = content
    mycomment.save()
    return _todetail(reqeust,blogid)

def index(request):
    bloglist = Blog.objects.all()
    return _toIndex(request,bloglist)

def _toIndex(request,bloglist):
    limit = 5
    paginator = Paginator(bloglist,limit)
    page = request.REQUEST.get('page')
    try:
        bloglist = paginator.page(page)
    except PageNotAnInteger:
        bloglist = paginator.page(1)
    except EmptyPage:
        bloglist = paginator.page(paginator.num_pages)
    return render(request,'blog/index.html',{"bloglist":bloglist})

def search(request):
    keyword = request.POST["keyword"]
    bloglist = Blog.objects.filter(content__contains=keyword)
    return _toIndex(request,bloglist)

def searchbycategory(request):
    categoryid = request.REQUEST.get("categoryid")
    ct = Category.objects.get(id=categoryid)	
    bloglist = Blog.objects.filter(category=ct)
    return _toIndex(request,bloglist)
