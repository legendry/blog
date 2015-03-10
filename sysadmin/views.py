#encoding=utf8
from django.shortcuts import render
from blog.models import *
from django.http.response import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

def manage_login(request):
    if request.method == 'GET':
        user = request.session.get("user",None)
        if user and user.is_authenticated():
            return HttpResponseRedirect(reverse('sysadmin.views.manage_blog'))
        return render(request,'sysadmin/login.html')
    else:
        username = request.REQUEST.get('username')
        password = request.REQUEST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            request.session["user"] = user
            print (reverse('sysadmin.views.manage_blog'))
            return HttpResponseRedirect(reverse('sysadmin.views.manage_blog'))
        else:
            errmsg = '用户名和密码不匹配2'
            return render_to_response('sysadmin/login.html', RequestContext(request,{"errmsg":errmsg}))
                  
def manage_logout(request):
    auth.logout(request)
    request.session['user'] = None
    return render_to_response('sysadmin/login.html')

def _getCategoryList():
    return  Category.objects.all()

@login_required
def manage_blog(request):
    bloglist = Blog.objects.all()
    categories = _getCategoryList()
    return render(request,'sysadmin/manage.html',{"categories":categories,"bloglist":bloglist})

@login_required
def addcategory(reqeust):
    if reqeust.method == 'GET':
        return render(reqeust,'addcategory.html')
    else:
        cname = reqeust.REQUEST.get("category_name")
        ct = Category.objects.create()
        ct.category_name=cname
        print('categoryname=%s' % cname)
        try:
            ct.save()
            return HttpResponseRedirect('/')
        except:
            errmsg = "create category failed"
            return render(reqeust,'sysadmin/error.html',{"errmsg":errmsg})

@login_required     
def addblog(request):
    if request.method == 'GET':
        categories = _getCategoryList()
        return render(request,'addblog.html',{'categories':categories})
    else:
        mysubject =request.REQUEST.get("subject")
        mycontent =request.REQUEST.get("content")
        mycategoryid = request.REQUEST.getlist("categoryid")[0]
        mycategory = Category.objects.get(id=mycategoryid)
        create_time = datetime.now()
        myblog = Blog.objects.create(subject=mysubject,content=mycontent,category=mycategory,create_time=create_time)
        try:
            myblog.save()
            return HttpResponseRedirect('/')
        except:
            errmsg = "create blog failed"
            return render(request,'sysadmin/error.html',{"errmsg":errmsg})

@login_required     
def updateblog(request):
    if request.method == 'GET':
        categories = _getCategoryList()
        blogid = request.REQUEST.get("blogid")
        blog = Blog.objects.get(id=blogid)
        return render(request,'sysadmin/updateblog.html',{'categories':categories,"blog":blog})
    else:
        myblogid = request.REQUEST.get("blogid")
        mysubject =request.REQUEST.get("subject")
        mycontent =request.REQUEST.get("content")
        mycategoryid = request.REQUEST.getlist("categoryid")[0]
        mycategory = Category.objects.get(id=mycategoryid)
        myblog = Blog.objects.filter(id=myblogid)
        try:
            myblog.update(subject=mysubject,content=mycontent,category=mycategory)
            return HttpResponseRedirect(reverse('sysadmin.views.manage_blog'))
        except:
            errmsg = "update blog failed"
            return render(request,'sysadmin/error.html',{"errmsg":errmsg})  
      
def _todetail(request,blogid):
    categories = _getCategoryList()
    myblog = Blog.objects.get(id=blogid)
    return render(request,'sysadmin/detail.html',{"blog":myblog,'categories':categories})
      
def detail(request,blogid):
    return _todetail(request,blogid)   

def index(request):
    bloglist = Blog.objects.all()
    categories = _getCategoryList()
    return _toIndex(request,bloglist,categories)

def _toIndex(request,bloglist,categories):
    limit = 5
    paginator = Paginator(bloglist,limit)
    page = request.REQUEST.get('page')
    try:
        bloglist = paginator.page(page)
    except PageNotAnInteger:
        bloglist = paginator.page(1)
    except EmptyPage:
        bloglist = paginator.page(paginator.num_pages)
    return render(request,'blog/index.html',{"bloglist":bloglist,'categories':categories})

def search(request):
    keyword = request.REQUEST.get("keyword")
    bloglist = Blog.objects.filter(content__contains=keyword)
    categories = _getCategoryList()
    return _toIndex(request,bloglist,categories)

def searchbycategory(request):
    categoryid = request.REQUEST.get("categoryid")
    ct = Category.objects.get(id=categoryid)	
    bloglist = Blog.objects.filter(category=ct)
    categories = _getCategoryList()
    return _toIndex(request,bloglist,categories)
