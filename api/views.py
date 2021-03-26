from urllib.parse import quote_plus

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import PostSerializer, SectionSerializer
from blog.filters import ModelFilter
from blog.models import Post, Section


@api_view(['GET'])
def apiOverView(request):
    api_list = {
        'list': 'api/PostList/',
        'filterlist': 'api/filterBlog/',
        'post': 'api/postDetail/<int:pk>',


    }
    return Response(api_list)


@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    sections = Section.objects.filter(post=post)
    context = {
        "request": request,
    }
    post_serializer = PostSerializer(post,many=False,context=context)
    section_serializer = SectionSerializer(sections, many=True,context=context)
    share_string = {'title':quote_plus(post.title),'summery':post.description[0:20]}
    response = {'post':post_serializer.data,'section':section_serializer.data,'share_string':share_string}
    return Response(response)

@api_view(['GET'])
def filterBlog(request,text):
    posts = Post.objects.all()
    item = text
    posts = ModelFilter(model_objects=posts, item=item).filter()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)
