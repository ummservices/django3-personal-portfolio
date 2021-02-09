from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    blogs_count = Blog.objects.all()
    return render(request, 'blog/all_blogs.html',{'blogs':blogs, 'blogscount':blogs_count})


def detail(request, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/details.html',{'blog':blog})
