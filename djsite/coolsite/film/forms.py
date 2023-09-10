from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *
from captcha.fields import CaptchaField

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        # Внутри класса Meta определена модель, с которой связана форма (Film), и указаны поля, которые должны быть отображены в форме. Также определены виджеты для некоторых полей, чтобы задать им определенные атрибуты или стили.
        model = Film
        fields = ['title','slug','content','photo','is_published','cat']

        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-input'}),
                    'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        #Класс Meta в Django используется для определения дополнительных настроек модели или формы. Он позволяет задать различные метаданные и конфигурации, связанные с моделью или формой.
        #Класс Meta предоставляет способ задать дополнительные настройки для модели или формы в одном месте, что делает код более организованным и позволяет легко настраивать поведение модели или формы в централизованном месте.
        model = User
        fields = ('username', 'email','password1','password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()