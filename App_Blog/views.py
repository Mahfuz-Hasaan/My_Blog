from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import BlogForm
from .models import Blog
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.http import HttpResponseRedirect


class CreateBlog(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'App_Blog/create_blog.html'
    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ','-') + '-' + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:blog_list'))

class BlogList(ListView):
    model = Blog
    template_name = 'App_Blog/blog_list.html'
    context_object_name = 'blogs'