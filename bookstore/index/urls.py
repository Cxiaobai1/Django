# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 21:37
# @Author  : Cxiaobai
# @Email   : 494158341@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path

from . import views
from index.views import LoginView

app_name = 'index'
urlpatterns = [
    path('', views.test_index, name='index'),
    path('test/', views.test, name='test'),
    path('book_name/', views.Book_name, name='book_name'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('set_cookie/', views.set_cookie_view, name='set_cookie'),
    path('get_cookie/', views.get_cookie_view, name='get_cookie'),
    path('title_search/', views.title_search, name='title_search'),
    path('title_search_result/', views.title_search_result, name='title_search_result'),
    path('book_table/', views.book_table, name='book_table'),
    path('add_book/', views.add_book, name='add_book'),
]
