from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from urllib.parse import quote_plus

from blog.filters import ModelFilter
from blog.models import Post, Section


def home(request):
    posts = Post.objects.all()
    if request.POST:
         item = request.POST.get('text')
         posts = ModelFilter(model_objects=posts, item=item).filter()
         posts = serializers.serialize("json", posts)
         response = JsonResponse({'posts': posts})
         return response
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)


def post(request,pk):
    post = Post.objects.get(id=pk)
    sections = Section.objects.filter(post=post)
    share_string = quote_plus(post.title)
    context = {'post':post, 'sections':sections,'share_string':share_string}
    return render(request, 'blog/post.html', context)