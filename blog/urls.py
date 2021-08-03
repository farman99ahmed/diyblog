from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.get_authors, name='get_authors'),
    path('authors/<int:id>', views.get_author, name='get_author'),
    path('authors/add', views.post_put_author, name='post_author'),
    path('authors/add/<int:id>', views.post_put_author, name='put_author'),
    path('authors/delete/<int:id>', views.delete_author, name='delete_author'),
]