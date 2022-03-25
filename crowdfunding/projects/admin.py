from django.contrib import admin
from .models import Project, Category
# Register your models here.

from django.contrib import admin
from .models import Category, Project

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username']

# admin.site.register(CustomUser, CustomUserAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'goal', 'category']

admin.site.register(Project, ProjectAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']

admin.site.register(Category, CategoryAdmin)







