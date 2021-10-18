from django.contrib import admin

from .models import Author, UserInfo,AllBook


# Register your models here.


@admin.register(AllBook)
class AllBookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ['username']
