# from email.mime import image
# from unicodedata import category
# from unittest.util import _MAX_LENGTH
# from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import Project, Pledge, Category, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.SlugRelatedField(
        slug_field= 'username', 
        queryset= get_user_model().objects.all()
    )
    # supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    # pledge_type = PledgeTypeSerializer(many=False, read_only=False)
    supporter = serializers.ReadOnlyField(source='supporter.id')

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)



class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    # category = CategorySerializer(many=False, read_only=False)
    goal = serializers.IntegerField()
    # goal_date = serializers.DateTimeField()
    # progress = serializers.IntegerField()
    image = serializers.URLField()
    status = serializers.CharField(max_length=200)
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # pledges = PledgeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')


    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only="true",
    )

    class Meta:
        model = Comment
        # fields = []
        exclude = ["visible"]


class ProjectCommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only="true",
        # queryset=User.objects.all()
    )

    class Meta:
        model = Comment
        # fields = []
        exclude = ["visible", "project"]        


class ProjectDetailSerializer(ProjectSerializer):
    # description = serializers.CharField(max_length=200)
    # image = serializers.URLField()
    pledges = PledgeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
          instance.title = validated_data.get('title', instance.title)
          instance.description = validated_data.get('description', instance.description)
          instance.goal = validated_data.get('goal', instance.goal)
        #   instance.goal_date = validated_data.get('goal_date', instance.goal_date)
          instance.image = validated_data.get('image', instance.image)
          instance.is_open = validated_data.get('is_open', instance.is_open)
          instance.category = validated_data.get('category',instance.category)
          instance.date_created = validated_data.get('date_created', instance.date_created)
          instance.owner = validated_data.get('owner', instance.owner)
          instance.save()
          return instance

class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField()
        
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
# and a link within ProjectSerializer
# category = CategorySerializer(many=False, read_only=False)
