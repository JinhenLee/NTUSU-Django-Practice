from django.urls import path
from .views import logout_view, SignUp

app_name = 'users'
urlpatterns = [
    path('logout/', logout_view, name = 'logout'),
    path('signup/', SignUp.as_view(), name = 'signup'),
]

#https://www.onespacemedia.com/news/getting-started-generic-class-based-views-django/