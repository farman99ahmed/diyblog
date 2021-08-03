from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.get_authors, name='get_authors'),
    path('authors/<int:id>', views.get_author, name='get_author'),
    path('authors/add', views.post_put_author, name='post_author'),
    path('authors/add/<int:id>', views.post_put_author, name='put_author'),
    path('authors/delete/<int:id>', views.delete_author, name='delete_author'),

    path('', views.get_blogs, name='get_blogs'),
    path('blogs/', views.get_blogs, name='get_blogs'),
    path('blogs/<int:id>', views.get_blog, name='get_blog'),
    path('blogs/add', views.post_put_blog, name='post_blog'),
    path('blogs/add/<int:id>', views.post_put_blog, name='put_blog'),
    path('blogs/delete/<int:id>', views.delete_blog, name='delete_blog'),

    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]