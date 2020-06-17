from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.
def blog(request):
    template = "blog/blog.html"
    posts = Post.objects.all()
    return render(request, template, {'posts': posts})

def category(request, category_id):
    template = 'blog/category.html'
    category = get_object_or_404(Category, id=category_id)
    return render(request, template, {'category': category} )