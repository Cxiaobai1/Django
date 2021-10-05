import hashlib

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Author, UserInfo, BOOk, Pub_name
from django import forms


# Create your views here.

def test_index(request):
    a = {}
    a['name'] = {'a': '1', 'b': '2'}
    return render(request, 'index/index.html', a)


def test(request):
    return render(request, 'index/test.html')


def Book_name(request):
    # Books = BOOk.objects.raw("select * from index_book")
    BOOKs = BOOk.objects.get(title='Python')
    return render(request, "index/book_name.html", locals())


# FBV
def login(request):
    if request.method == 'get':
        return HttpResponse("登陆成功")
    elif request.method == 'post':
        return HttpResponse("0")


# CBV
class LoginView(View):
    def get(self, request):
        return HttpResponse("登陆成功")

    def post(self, request):
        return HttpResponse("0")


# 表单系统简单应用
class Loginforms(forms.Form):
    user_name = forms.CharField(label='用户名', min_length=6, max_length=12)
    user_password = forms.CharField(label='密码', min_length=8)


def logins(request):
    if request.method == "post":
        form = Loginforms(request.POST)
        if form.is_valid():
            return HttpResponse("登陆成功")
    else:
        form = Loginforms()
    return render(request, "index/login.html", locals())


def set_cookie_view(request):
    resp = HttpResponse()
    resp.set_cookie('username', 'wuchangyu', 3600)
    return resp


def get_cookie_view(request):
    value = request.COOKIES.get('username')
    return HttpResponse('--MY COOKIE is--%s' % value)


def login_view(request):
    if request.method == "GET":
        if 'username' in request.session:
            return HttpResponseRedirect('/index/test')
        if 'username' in request.COOKIES:
            request.session['usename'] = request.COOKIES['username']
            return HttpResponseRedirect('/index/test')
        return render(request, 'index/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        password_m = m.hexdigest()
        print(password_m)
        if not username or not password:
            error = '你输入的用户名或密码错误！'
            return render(request, 'index/login.html', locals())
        users = UserInfo.objects.filter(username=username, password=password)  # 密码未使用哈希加密
        if not users:
            error = '用户不存在或密码错误'
            return render(request, 'index/login.html', locals())
        users = users[0]
        request.session['username'] = username
        response = HttpResponseRedirect('/index/test')
        if 'isSaved' in request.POST.keys():
            response.set_cookie('username', username, 60 * 60 * 24 * 7)
        return response


def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    resp = HttpResponseRedirect('/index/login')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    return resp


def register_view(request):
    if request.method == 'GET':
        return render(request, 'index/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            username_error = '请输入正确的用户名'
            return render(request, 'index/register.html', locals())
        password = request.POST.get('password')
        md = hashlib.md5()
        md.update(password.encode('utf-8'))
        password_md = md.hexdigest()
        password_again = request.POST.get('password_again')
        md = hashlib.md5()
        md.update(password_again.encode('utf-8'))
        password_again_md = md.hexdigest()
        if not password_md or not password_again_md:
            password_error = "请输入正确的密码"
            return render(request, 'index/register.html', locals())
        if password_md != password_again_md:
            password_again_error = "请输入一致的密码"
            return render(request, 'index/register.html', locals())
        try:
            UserInfo.objects.get(username=username)
            username_error = "该用户名已被注册"
            return render(request, 'index/register.html', locals())
        except Exception as e:
            print("%s 是可用的用户名-%s" % (username, e))
            try:
                UserInfo.objects.create(username=username, password=password_again_md)
                request.session['username'] = username
                return render(request, 'index/test.html')
            except Exception as e:
                print(e)
                username_error = '该用户名已被占用'
                return render(request, 'index/register.html', locals())


def title_search(request):
    if not request.GET.get('title', 0):
        error = ["书名无效"]
        return render(request, 'index/title_search.html', locals())
    return render(request, 'index/title_search_result.html')


def title_search_result(request):
    title = BOOk.objects.filter(title__icontains=request.GET['title'])
    print(title)
    if not title:
        error = "没有找到"
    return render(request, 'index/title_search_result.html', locals())


def book_table(request):
    try:
        all_book = BOOk.objects.all().order_by('id')
        if not all_book:
            return HttpResponse("书籍记录为空")
    except Exception as e:
        print(e)
    return render(request, 'index/book_table.html', locals())


def add_book(request):
    if request.method == 'GET':
        return render(request, 'index/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        if not title:
            return HttpResponse('请输入正确的书籍名称')
        price = float(request.POST.get('price', 999.99))
        if not price:
            return HttpResponse('请驶入价格')
        pub = request.POST.get('public')
        try:
            retail_price = request.POST.get('retail_price')
            if not retail_price:
                return HttpResponse('请输入市场价')
        except Exception as e:
            print(e)

        old_title = BOOk.objects.filter(title=title)
        if old_title:
            return HttpResponse('该书籍已存在')
        try:
            pub1 = Pub_name.objects.get(pubname=str(pub))
            BOOk.objects.create(title=title, price=price, retail_price=retail_price, pub=pub1)
        except Exception as e:
            print("Add ErrorReason is %s" % e)
        return HttpResponseRedirect('/index/book_table')
    return HttpResponse("请使用正确的HTTP请求方式！")


def delete_book(request):
    pass
