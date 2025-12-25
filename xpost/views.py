from django.shortcuts import render

from xpost.models import Post



def xpost_home (request):
    posts = Post.objects.all()
    if posts:
        posts=posts
    else:
        posts=None
    context = dict (
        posts=posts,
    )
    return render (request,"main/xpost-home.html",context)


