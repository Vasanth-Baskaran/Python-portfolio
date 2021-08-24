from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def all_blogs_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs':blogs})