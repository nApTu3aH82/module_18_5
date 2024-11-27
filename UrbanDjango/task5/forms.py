from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label='Введите пароль', min_length=8, required=True)
    rpt_password = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль', min_length=8, required=True)
    age = forms.IntegerField(label='Введите свой возраст:', required=True)
