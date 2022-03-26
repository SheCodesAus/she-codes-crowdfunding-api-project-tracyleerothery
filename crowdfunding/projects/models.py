# from turtle import title
from email.quoprimime import body_check
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.

# class BaseModel(models.Model)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    # goal_date = models.DateTimeField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
        )


    category = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='project_id'
    )

    def __str__(self):
        return self.title


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    # supporter =models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
        )


# created a class for category
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.title

# added a link from projects to categories

# category = models.ForeignKey(
#         'Category',
#         null=True, blank=True,
#         on_delete=models.CASCADE,
#         related_name='project_id'
#     )


class Comment(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    body = models.TextField()
    visible = models.BooleanField(default=True)


    


