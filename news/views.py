from django.shortcuts import render
from news.models import Post
# Create your views here.
def bloghome(request): 
    allPosts= Post.objects.all()
    context={'a': allPosts}
    return render(request, "news/bloghome.html", context)    

def blogpost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    params={"post":post}
    return render(request, "news/blogpost.html", params)