from rest_framework import serializers
from blog.models import Post, Section
from illustrations.models import Svg


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SvgSerializer(serializers.ModelSerializer):

    class Meta:
        model = Svg
        fields = '__all__'
