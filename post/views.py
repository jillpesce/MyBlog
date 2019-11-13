from django.shortcuts import render
from post.models import Post
import markdown2


def splash(request):
    posts = Post.objects.all()
    return render(request, "splash.html", {"posts": posts})

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts": posts})
	
def post(request, id):
    post = Post.objects.get(id = id)
    post.description = markdown2.markdown(post.description)
    post.title= markdown2.markdown(post.title)
    post.date = markdown2.markdown(post.date)
    post.author = markdown2.markdown(post.author)
    return render(request, "post.html", {"post": post})

