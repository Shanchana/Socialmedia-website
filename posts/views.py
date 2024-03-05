from django.shortcuts import render,redirect
from .models import Post

def home(request):
     posts = Post.objects.all().order_by('-created_at')
     return render(request, 'posts/home.html', {'posts': posts})

def create_post(request):
     if request.method == 'POST':
         title = request.POST['title']
         content = request.POST['content']
         post = Post(title=title, content=content)
         post.save()
         return redirect('home')
     return render(request, 'posts/create_post.html')