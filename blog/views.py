from django.shortcuts import render, redirect
from .forms import AuthorForm, BlogForm, NewUserForm
from .models import Author, Blog
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required

# Create your views here.

def get_authors(request):
    context = {'authors': Author.objects.all()}
    return render(request, "blog/get_authors.html", context)

@login_required
def get_author(request, id):
    author =  Author.objects.get(pk = id)
    blogs = Blog.objects.filter(author = id)
    context = {'author': author, 'blogs': blogs}
    return render(request, "blog/get_author.html", context)

@login_required
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

@login_required
def delete_author(request, id):
    author = Author.objects.get(pk = id)
    author.delete()
    return redirect('get_authors')

def get_blogs(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, "blog/get_blogs.html", context)

@login_required
def get_blog(request, id):
    blog = {'blog': Blog.objects.get(pk = id)}
    return render(request, "blog/get_blog.html", blog)

@login_required
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

@login_required
def delete_blog(request, id):
    blog = Blog.objects.get(pk = id)
    blog.delete()
    return redirect('get_blogs')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("get_blogs")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="blog/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("get_blogs")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="blog/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("get_blogs")
