from urllib.request import Request
from django.shortcuts import render
from .models import Post
from .form import PostForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    posts=Post.objects.all()

    return render(request,'index.html',{
        'posts':posts
    })
def post(request,pk):
    posts=Post.objects.get(id=pk)
    return render(request,'post.html',{
        'posts':posts
    })
def edit(request,pk):
    posts=Post.objects.get(id=pk)

    form=PostForm(request.POST or None,instance=posts)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'edit.html',{
        'form':form
    })
def add(request):
    submited=False
    if request.method =="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/add?submited=True')
    else:
        form=PostForm
        if 'submited' in request.GET:
            submited=True





        
    
    return render(request,"add.html",{'form':form,'submit':submited})