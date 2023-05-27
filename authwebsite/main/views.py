from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from main.forms import LoginForm, RegisterForm
# Create your views here.

# главная страница
def index(request):
    # return HttpResponse("<h1>Первая страница</h1>")
    return render(request, 'main/pages/home.html')

def loginPage(request):
    return render(request, 'main/pages/login.html')

def registerPage(request):
    return render(request, 'main/pages/registration.html')

def me(request):
    # если не авторизован, то редирект на страницу входа
    if not request.user.is_authenticated:
        return redirect('login')
    # рендерим шаблон и передаем туда объект пользователя
    return render(request, 'main/pages/me.html', {'user': request.user})

# выход
def doLogout(request):
    # вызываем функцию django.contrib.auth.logout и делаем редирект на страницу входа
    logout(request)
    return redirect('login')

# страница входа
def loginPage(request):
    # инициализируем объект класса формы
    form = LoginForm()

    # обрабатываем случай отправки формы на этот адрес
    if request.method == 'POST':

        # заполянем объект данными, полученными из запроса
        form = LoginForm(request.POST)

        # проверяем валидность формы
        if form.is_valid():
            # пытаемся авторизовать пользователя
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # если существует пользователь с таким именем и паролем,
                # то сохраняем авторизацию и делаем редирект
                login(request, user)
                return redirect('me')
            else:
                # иначе возвращаем ошибку
                form.add_error(None, 'Неверные данные!')

    # рендерим шаблон и передаем туда объект формы
    return render(request, 'main/pages/login.html', {'form': form})

def registerPage(request):
    # return render(request, 'main/pages/registration.html')
    # инициализируем объект формы
    form = RegisterForm()

    if request.method == 'POST':
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)

        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # По-моему, более логично сразу логинить юзера после регистрации и отправлять в ЛК
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('me')
        
            # return redirect('login')
    # ренедерим шаблон и передаем объект формы
    return render(request, 'main/pages/registration.html', {'form': form})

