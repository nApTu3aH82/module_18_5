from django.shortcuts import render
from .forms import UserRegister
# Create your views here.

users = ['Rinat', "Marat", "Sofia", "Alina"]


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        rpt_password = request.POST.get('rpt_password')
        age = request.POST.get('age')
        if password != rpt_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18!'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
            info['message'] = f'Приветствуем, {username}!'
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            rpt_password = form.cleaned_data['rpt_password']
            age = form.cleaned_data['age']
            if password != rpt_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18!'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append(username)
                info['message'] = f'Приветствуем, {username}!'
    return render(request, 'fifth_task/registration_page.html', info)