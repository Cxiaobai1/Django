from django.contrib import admin

from .models import BOOk, Author, UserInfo


# Register your models here.


@admin.register(BOOk)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'pub__pubname']
    list_display = ['id', 'title', 'price']
    list_filter = ['price']
    raw_id_fields = ['pub']
    list_editable = ['price']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ['username']
