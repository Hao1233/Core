from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout

# Create your views here.
from .models import *
from .forms import CreatePostForm,CreateUserForm, CreateCommentForm
def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,"OurProfile/home.html",context)
def posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,"OurProfile/posts.html",context)
def post(request,pk):
    post = Post.objects.get(pk=pk)
    comments = CreateCommentForm()
    if request.method == 'POST':
        comments = CreateCommentForm(request.POST)
        if comments.is_valid():
            comments.instance.post_id = pk
            comments.instance.customer_comment = request.user
            comments.save()
            return redirect('post', post.id)
    context={'post':post, 'comments':comments}
    return render(request,"OurProfile/post.html",context)
def createpost(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if form.is_valid(): 
                form.instance.customer = request.user
                form.save() 
                return redirect('posts')
    context = {'form':form}
    return render(request,"OurProfile/create_post_form.html",context)
def createuser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render(request,"OurProfile/register_form.html",context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
    return render(request,"OurProfile/login_form.html")
def logout(request):
    django_logout(request)
    return render(request,"OurProfile/home.html")
def comment(request,pk):
    post = Post.objects.get(pk=pk)
    comments = CreateCommentForm()
    if request.method == 'POST':
        comments = CreateCommentForm(request.POST)
        if comments.is_valid():
            comments.instance.post_id = pk
            comments.instance.customer_comment = request.user
            comments.save()
            return redirect('post', post.id)
    context={'comments':comments}
    return render(request,"OurProfile/post.html",context)