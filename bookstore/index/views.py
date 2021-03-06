import hashlib
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Author, UserInfo, BOOk, Pub_name, MfBook, AllBook
from .forms import TitleSearch, NameForm, RegisterForm, LoginForm
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    return render(request, 'index/index.html')


def login_view(request):
    if request.method == "GET":
        if 'username' in request.session:
            return render(request, 'index/index.html')
        if 'username' in request.COOKIES:
            request.session['usename'] = request.COOKIES['username']
            return render(request, 'index/index.html')
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # print(email)
            m = hashlib.md5()
            m.update(password.encode('utf-8'))
            password_m = m.hexdigest()
            # print(password_m)
            users = UserInfo.objects.filter(email=email, password=password_m)  # 密码未使用哈希加密
            # print(users)
            if not users:
                error = '用户不存在或密码错误'
                return render(request, 'index/login.html', locals())
            users = users[0]
            request.session['username'] = email
            response = HttpResponseRedirect('/index')
            if 'isSaved' in request.POST.keys():
                response.set_cookie('email', email, 60 * 60 * 24 * 7)
            return render(request, 'index/index.html', locals())
    return render(request, 'index/login.html', locals())


def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    resp = HttpResponseRedirect('/index/login')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    return resp


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            username = form.cleaned_data['username']

            md = hashlib.md5()
            md.update(password.encode('utf-8'))
            password_md = md.hexdigest()
            md = hashlib.md5()
            md.update(password_again.encode('utf-8'))
            password_again_md = md.hexdigest()
            if password_md != password_again_md:
                password_again_error = "请输入一致的密码"
                return render(request, 'index/register.html', locals())
            print(email)
            try:
                UserInfo.objects.get(email=email)
                username_error = "该邮箱已被注册"
                return render(request, 'index/register.html', locals())
            except Exception as e:
                print("%s 是可用的邮箱-%s" % (email, e))
                try:
                    UserInfo.objects.create(username=username, email=email, password=password_again_md)
                    request.session['email'] = email
                    return render(request, 'index/index.html')
                except Exception as e:
                    print(e)
                    username_error = '注册失败'
                    return render(request, 'index/register.html', locals())
    return render(request, 'index/register.html', locals())


def title_search(request):
    if not request.GET.get('title', 0):
        error = ["书名无效"]
        return render(request, 'index/title_search.html', locals())
    return render(request, 'index/title_search_result.html')


def title_search_result(request):
    title = BOOk.objects.filter(title__icontains=request.GET['title'])
    # print(title)
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
    if request.method == 'GET':
        return render(request, 'index/delete_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')

        title_search = BOOk.objects.filter(title=title)
        # print(title_search)
        if not title_search:
            error = '该书籍不存在'
            return render(request, 'index/delete_book.html', locals())

        else:
            title_search.delete()
            return HttpResponseRedirect('/index/book_table')
    else:
        return HttpResponse('请使用正确的HTTP请求方式！')
    pass


def search_title_form(request):
    return render(request, 'index/title_search.html', context={'form': TitleSearch})


def search_title(request):
    form = TitleSearch(request.GET)
    if form.is_valid():
        books = BOOk.objects.filter(title__icontains=form.cleaned_data['title'])
        if not books:
            return HttpResponse('没有此书籍')
        return render(request, 'index/title_search_result', locals())
    else:
        return render(request, 'index/title_search.html', {'form': form})


def cx(request):
    return render(request, 'index/畅销榜.html')


def dy(request):
    return render(request, 'index/订阅榜.html')


def dj(request):
    return render(request, 'index/点击榜.html')


def mf(request):
    mf_books = MfBook.objects.all()
    paginator = Paginator(mf_books, 20)
    num_p = request.GET.get('page', 1)
    page = paginator.page(int(num_p))
    # print(page)
    return render(request, 'index/免费榜.html', locals())


def xs(request):
    return render(request, 'index/新书榜.html')


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)

        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            return HttpResponse('your_name:%s' % your_name)
    else:
        form = NameForm()
    return render(request, 'index/name.html', {'form': form})
    pass


def click_title(request):
    if request.method == 'GET':
        book = AllBook.objects.all()
    pass


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return HttpResponse('你好')
    else:
        form = RegisterForm()
    return render(request, 'index/register.html', locals())
    pass
