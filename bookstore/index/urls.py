from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('title_search_result/', views.title_search_result, name='title_search_result'),
    path('book_table/', views.book_table, name='book_table'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('name_form/', views.get_name, name='name_form'),
    path('cx/', views.cx, name='cx'),
    path('dy/', views.dy, name='dy'),
    path('dj/', views.dj, name='dj'),
    path('mf/', views.mf, name='mf'),
    path('xs/', views.xs, name='xs'),
    path('description/', views.click_title, name='description'),
]
