from django.urls import path
from api.views import *
urlpatterns = [
    path('', apiOverView, name='apiOverView'),
    path('postList/', postList, name='postList'),
    path('filterBlog/<str:text>', filterBlog, name='filterBlog'),
    path('postDetail/<int:pk>', postDetail, name='postDetail'),
]
