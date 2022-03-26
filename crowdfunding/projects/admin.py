from django.contrib import admin
from .models import Project, Category, Pledge
# Register your models here.

from django.contrib import admin
from .models import Category, Project, Pledge
 
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username']

# admin.site.register(CustomUser, CustomUserAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'goal', 'category', 'date_created']

admin.site.register(Project, ProjectAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']

admin.site.register(Category, CategoryAdmin)


class PledgeAdmin(admin.ModelAdmin):
    list_display = ['amount', 'comment', 'anonymous', 'project'] 

admin.site.register(Pledge, PledgeAdmin)







