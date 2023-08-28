from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def blogs(request):
    allPosts = Blog.objects.all()
    allPosts = reversed(allPosts)
    context = {'posts' : allPosts}
    return render(request, 'blogs.html', context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog' :blog}
    return render(request, 'blogpost.html', context)