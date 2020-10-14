from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import SignUpForm

# Create your views here.
class SignUp(FormView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username, 'email@email', password)
        user.save()
        return redirect('blog:list')

def logout_view(request):
    logout(request)
    return redirect('blog:list')