from django.shortcuts import render, get_object_or_404
from .models import Post
def homePage(request):
    post = Post.objects.all().order.by('-postDate')

    return render(request, "index.html", {
        'posts': posts
    })

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post-deetail.html", {
        'post':post
    })

# Create your views here.
def aboutPage(request):
    title = "About"
    return render(request, "about.html" {
        'title' : title
    })
# Create your views here.