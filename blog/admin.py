from django.contrib import admin
from .models import UserProfile, Post, Comment

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    pass


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post, PostAdmin)
