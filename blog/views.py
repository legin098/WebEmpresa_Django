from webbrowser import get
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def blog(request):
  return render(request, 'blog/blog.html', {'posts': Post.objects.all()})

def category(request, category_id):
  category = get_object_or_404(Category, id=category_id)
  return render(request, 'blog/category.html', {'category': category})