from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog , pk=blog_id)
    return render(request,'detail.html', {'blog':blog_detail})

def new(request):
    form = BlogForm()
    return render(request,'new.html', {'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid:
        form.save()
    return redirect('home')

def edit(request,blog_id):
    edit_blog = Blog.objects.get(id=blog_id)
    form = BlogForm(instance=edit_blog)
    return render(request, 'edit.html',{'form':form, 'blog':edit_blog})

def update(request, blog_id):
    if request.method=="POST":
        update_blog = Blog.objects.get (id = blog_id)
        form = BlogForm(request.POST, request.FILES, instance=update_blog)
        form.save()
    return redirect('home')

def delete(request, blog_id):
    delete_blog = Blog.objects.get(id=blog_id)
    delete_blog.delete()
    return redirect('home')