from django.shortcuts import render, redirect
from .forms import AuthorForm, BlogForm
from .models import Author, Blog

# Create your views here.

def get_authors(request):
    context = {'authors': Author.objects.all()}
    return render(request, "blog/get_authors.html", context)

def get_author(request, id):
    author =  Author.objects.get(pk = id)
    blogs = Blog.objects.filter(author = id)
    context = {'author': author, 'blogs': blogs}
    return render(request, "blog/get_author.html", context)

def post_put_author(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk = id)
            form = AuthorForm(instance = author)
        return render(request, "blog/post_put_authors.html", {"form": form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk = id)
            form = AuthorForm(request.POST, instance = author)
        if form.is_valid():
            form.save()
        return redirect('get_authors')

def delete_author(request, id):
    author = Author.objects.get(pk = id)
    author.delete()
    return redirect('get_authors')

def get_blogs(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, "blog/get_blogs.html", context)

def get_blog(request, id):
    blog = {'blog': Blog.objects.get(pk = id)}
    return render(request, "blog/get_blog.html", blog)

def post_put_blog(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = BlogForm()
        else:
            blog = Blog.objects.get(pk = id)
            form = BlogForm(instance = blog)
        return render(request, "blog/post_put_blogs.html", {"form": form})
    else:
        if id == 0:
            form = BlogForm(request.POST)
        else:
            blog = Blog.objects.get(pk = id)
            form = BlogForm(request.POST, instance = blog)
        if form.is_valid():
            form.save()
        return redirect('get_blogs')

def delete_blog(request, id):
    blog = Blog.objects.get(pk = id)
    blog.delete()
    return redirect('get_blogs')
