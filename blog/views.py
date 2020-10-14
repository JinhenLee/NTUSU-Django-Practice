from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.  
class AllPost(ListView):
    model = Post

class ThisPost(DetailView):
    model = Post
    
class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:list')
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:list')
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_delete'
    success_url = reverse_lazy('blog:list')
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    success_url = reverse_lazy('blog:list')
    def post(self, request, pk):
        post = get_object_or_404(Post, id = pk)
        comment = Comment(content = request.POST['content'], owner = request.user, post = post)
        comment.save()
        return redirect(reverse('blog:detail', args=[pk]))