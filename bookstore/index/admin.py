from django.contrib import admin

from .models import Author, UserInfo,AllBook


# Register your models here.


@admin.register(AllBook)
class AllBookAdmin(admin.ModelAdmin):
    search_fields = ['title','author']
    list_display = ['title','author']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ['username']
