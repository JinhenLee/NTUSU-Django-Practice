from django.urls import path
from .views import AllPost, ThisPost, AddPost, EditPost, DeletePost, AddComment

app_name = 'blog'
urlpatterns = [
    path('', AllPost.as_view(), name = 'list'),
    path('<int:pk>/', ThisPost.as_view(), name = 'detail'),
    path('add/', AddPost.as_view(), name = 'add'),
    path('<int:pk>/edit/', EditPost.as_view(), name = 'edit'),
    path('delete/<int:pk>/', DeletePost.as_view(), name = 'delete'),
    path('<int:pk>/comment/', AddComment.as_view(), name = 'addcomment'),
]

#https://www.onespacemedia.com/news/getting-started-generic-class-based-views-django/